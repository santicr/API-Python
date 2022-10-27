from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    lastname: str

class UpdateUserRequest(BaseModel):
    name: Optional[str]
    lastname: Optional[str]