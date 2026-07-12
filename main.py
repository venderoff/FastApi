from fastapi import FastAPI
from schema import User

app = FastAPI()

user_db = []

@app.get("/health")
def home():
    return {"message": "welcome to my API!",
    "health": "healthy",
    "status": "running"
    }

@app.get("/users")
def get_users():
     if not user_db:
         return {"users": "no users found"}
     return {"users": user_db}    
    

@app.post("/users")
def create_user(user: User):
    user_db.append(user)
    return {"message": "User created successfully", "user": user}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in user_db:
        if user.id == user_id:
            return {"user": user}
    return {"message": "User not found"}, 400

@app.put("/users/{user_id}")  
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(user_db):
        if user.id == user_id:
            user_db[index] = updated_user
            return {"message": "User updated successfully", "user": updated_user}
    return {"message": "User not found"}, 400

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(user_db):
        if user.id == user_id:
            del user_db[index]
            return {"message": "User deleted successfully"}
    return {"message": "User not found"}, 400