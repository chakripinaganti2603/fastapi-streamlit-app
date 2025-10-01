from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/greet")
def greet(name: str = "User"):
    return {"message": f"Hello, {name}!"}
