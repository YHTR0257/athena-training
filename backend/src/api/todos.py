import psycopg2.extras
from fastapi import APIRouter, HTTPException

from src.db import get_conn
from src.models import TodoCreate, TodoUpdate

router = APIRouter(prefix="/todos")


@router.get("")
def list_todos():
    with get_conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM todos ORDER BY id")
            return cur.fetchall()


@router.post("", status_code=201)
def create_todo(body: TodoCreate):
    with get_conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                "INSERT INTO todos (title) VALUES (%s) RETURNING *",
                (body.title,),
            )
            return cur.fetchone()


@router.patch("/{todo_id}")
def update_todo(todo_id: int, body: TodoUpdate):
    with get_conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM todos WHERE id = %s", (todo_id,))
            todo = cur.fetchone()
            if todo is None:
                raise HTTPException(status_code=404, detail="Not found")
            title = body.title if body.title is not None else todo["title"]
            done = body.done if body.done is not None else todo["done"]
            cur.execute(
                "UPDATE todos SET title = %s, done = %s WHERE id = %s RETURNING *",
                (title, done, todo_id),
            )
            return cur.fetchone()


@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM todos WHERE id = %s RETURNING id", (todo_id,))
            if cur.fetchone() is None:
                raise HTTPException(status_code=404, detail="Not found")
