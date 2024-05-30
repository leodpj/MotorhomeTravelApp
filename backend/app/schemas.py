from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ReviewBase(BaseModel):
    rating: int
    comment: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    user_id: int
    camping_id: int
    created_at: datetime

    class Config:
        orm_mode: True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    reviews: List[Review] = []

    class Config:
        orm_mode: True

class CampingBase(BaseModel):
    name: str
    location: str
    description: str
    price: float
    availability: str

class CampingCreate(CampingBase):
    pass

class Camping(CampingBase):
    id: int
    reviews: List[Review] = []

    class Config:
        orm_mode: True
