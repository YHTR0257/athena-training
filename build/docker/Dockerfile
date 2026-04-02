FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

# ============= Python dependencies =============
# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

COPY pyproject.toml uv.lock /app/
COPY src/ /app/src/
RUN uv sync --frozen --no-dev

# =============      End Python     =============

COPY main.py /app/
EXPOSE 8000
CMD ["uv", "run","fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]
