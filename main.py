from fastapi import FastAPI, Query, HTTPException
from typing import List
from pydantic import BaseModel, EmailStr
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return JSONResponse(content="pong", status_code=200, media_type="text/plain")

class User(BaseModel) :
    id : int
    name : str
    email : EmailStr

users = [
    {"id": 1, "name": "Alice", "email": "alice@gmail.com"},
    {"id": 2, "name": "Bob", "email": "alice@gmail.com"},
    {"id": 3, "name": "Charlie", "email": "alice@gmail.com"},
    {"id": 4, "name": "Diana", "email": "alice@gmail.com"},
    {"id": 5, "name": "Eve", "email": "alice@gmail.com"},
]

@app.get("/users", response_model=List[User])
def list_users(
        page: int = Query(1, ge=1, description="Numéro de la page (min 1)"),
        size: int = Query(20, ge=1, description="Nombre d'utilisateurs par page (min 1)")
):
    start = (page - 1) * size
    end = start + size

    result = users[start:end]

    if not isinstance(page, int) or not isinstance(size, int):
        raise HTTPException(
            status_code=400,
            detail="Bad types for provided query parameters"
        )

    return result

