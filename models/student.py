from pydantic import BaseModel
from typing import Optional
from models.address import Address, AddressUpdate


class Student(BaseModel):
    name: str
    age: int
    address: Address


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[AddressUpdate] = AddressUpdate()
