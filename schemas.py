from pydantic import BaseModel
from typing import List
class PostBase(BaseModel):
    title:str
    content:str

class PostCreate(PostBase):
      pass

class Post(PostBase):
     id:int
     owner_id:int
     

     class config:
          from_attribute=True
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        orm_mode = True