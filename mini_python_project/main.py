from fastapi import FastAPI
import uvicorn
import psycopg

app = FastAPI(title="Mini Python Project", version="0.1.0")

# Konfigurasi DB (sementara hardcode, nanti bisa env)
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 5432,
    "dbname": "appdb",
    "user": "userdev",
    "password": "devlinux1234/",
}

def get_one_user_name():
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name FROM users LIMIT 1;")
                row = cur.fetchone()
                if row:
                    return row[0]
    except Exception as e:
        print(f"DB error: {e}")

    return None


@app.get("/")
def read_root():
    name = get_one_user_name()
    if name:
        return {"message": f"Hello {name}, welcome to Mini Python Project!"}
    return {"message": "Hello World from Mini Python Project!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
