from fastapi import FastAPI
from models import User

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

