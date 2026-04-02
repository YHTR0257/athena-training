import { useEffect, useState } from 'react'
import { fetchTodos, createTodo, updateTodo, deleteTodo } from '../api/todos'

function Todo() {
  const [todos, setTodos] = useState([])
  const [input, setInput] = useState('')

  useEffect(() => {
    fetchTodos().then(setTodos)
  }, [])

  const handleCreate = async (e) => {
    e.preventDefault()
    if (!input.trim()) return
    const todo = await createTodo(input.trim())
    setTodos((prev) => [...prev, todo])
    setInput('')
  }

  const handleToggle = async (todo) => {
    const updated = await updateTodo(todo.id, { done: !todo.done })
    setTodos((prev) => prev.map((t) => (t.id === todo.id ? updated : t)))
  }

  const handleDelete = async (id) => {
    await deleteTodo(id)
    setTodos((prev) => prev.filter((t) => t.id !== id))
  }

  return (
    <div>
      <h1>TODO</h1>
      <form onSubmit={handleCreate}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="新しいタスク"
        />
        <button type="submit">追加</button>
      </form>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.done}
              onChange={() => handleToggle(todo)}
            />
            <span style={{ textDecoration: todo.done ? 'line-through' : 'none' }}>
              {todo.title}
            </span>
            <button onClick={() => handleDelete(todo.id)}>削除</button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default Todo
