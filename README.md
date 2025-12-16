# Mini Python Project

Project mini Python menggunakan Poetry dan Docker dengan FastAPI.

## Setup

### Menggunakan Poetry
```bash
# Install dependencies
poetry install

# Run aplikasi
poetry run start
```

### Menggunakan Docker
```bash
# Build image
docker build -t mini-python-project .

# Run container
docker run -p 8000:8000 mini-python-project
```

## Endpoints

- `GET /` - Hello World message
- `GET /health` - Health check

Aplikasi akan berjalan di http://localhost:8000