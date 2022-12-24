from fastapi import FastAPI
from models import User

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.put("/user/{id}")
def make_user(id: int, name: str, email: str):
    newUser = User(id = id, name = name, email = email)
    return(newUser.json())