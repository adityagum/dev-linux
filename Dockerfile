FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for psycopg
RUN apt-get update && apt-get install -y \
    libpq5 \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy poetry files
COPY pyproject.toml poetry.lock* ./

# Configure poetry
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --without dev --no-root

# Copy source code
COPY mini_python_project/ ./mini_python_project/

EXPOSE 8000

CMD ["poetry", "run", "start"]
