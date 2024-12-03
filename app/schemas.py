from pydantic import BaseModel
from typing import Optional

class AddressSchema(BaseModel):
    city: str
    country: str

class StudentCreate(BaseModel):
    name: str
    age: int
    address: AddressSchema

class StudentUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[AddressSchema]

class StudentResponse(BaseModel):
    id: str
    name: str
    age: int
    address: AddressSchema
