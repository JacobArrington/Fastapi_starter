from pydantic import BaseModel



class UserBase(BaseModel):
    email: str
    user_name: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
        
