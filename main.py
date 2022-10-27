from http.client import HTTPException
from socket import fromfd
from model import User, UpdateUserRequest
from fastapi import FastAPI

app = FastAPI()

db = [
    User(id = 1, name = "Carlos", lastname = "Mendez"),
    User(id = 2, name = "Andres", lastname = "Figueroa"),
    User(id = 3, name = "Camilo", lastname = "Silva")
]

@app.get('/')
def root():
    return {'Hello': 'World'}

@app.get('/api/users')
async def fetch_users():
    return db

@app.post('/api/users')
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete('/api/users/{user_id}')
async def delete_user(user_id: int):
    for user in db:
        if user.id == user_id:
            return db.remove(user)
    raise HTTPException(
        status_code = 404,
        detail = f"User with id:{user_id} does not exist"
    )

@app.put('/api/users/{user_id}')
async def update_user(user_id: int, new_user: UpdateUserRequest):
    for user in db:
        if user.id == user_id:
            if new_user.name is not None:
                user.name = new_user.name
            if new_user.lastname is not None:
                user.lastname = new_user.lastname
            return
    raise HTTPException(
        status_code = 404,
        detail = f"User with id:{user_id} does not exist"
    )