from fastapi import FastAPI
import uvicorn
import psycopg
import os

app = FastAPI(title="Mini Python Project", version="0.1.0")

DB_HOST = os.getenv("DB_HOST", "postgres-db")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "userdev")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

def get_one_user_name():
    dsn = f"host={DB_HOST} port={DB_PORT} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}"
    print(f"[DB] connecting: host={DB_HOST} port={DB_PORT} db={DB_NAME} user={DB_USER}")

    with psycopg.connect(dsn, connect_timeout=3) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM users ORDER BY id LIMIT 1;")
            row = cur.fetchone()
            print(f"[DB] result: {row}")
            return row[0] if row else None

@app.get("/")
def read_root():
    try:
        name = get_one_user_name()
        if name:
            return {"message": f"Hello {name} from Mini Python Project!"}
        return {"message": "No user found in DB"}
    except Exception as e:
        # Jangan ketelen—tampilkan error biar kelihatan di docker logs
        print(f"[DB] ERROR: {repr(e)}")
        return {"message": "Hello World from Mini Python Project!", "db_error": str(e)}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/db-check")
def db_check():
    # endpoint khusus untuk validasi DB tanpa mengubah root
    name = get_one_user_name()
    return {"db_host": DB_HOST, "first_user": name}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
