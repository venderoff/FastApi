from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., description="The unique identifier for the user")
    name: str = Field(..., description="The name of the user")
    email: str = Field(..., description="The email address of the user")
    is_active: bool = Field(default=True, description="Indicates if the user is active")