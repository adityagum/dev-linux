from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Mini Python Project", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Hello World from Mini Python Project!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()