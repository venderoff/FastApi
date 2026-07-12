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
     return {"users": user_db}    
    

@app.post("/users")
def create_user(user: User):
    user_db.append(user)
    return {"message": "User created successfully", "user": user}
