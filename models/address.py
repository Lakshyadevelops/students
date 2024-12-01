from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    city: str
    country: str


class AddressUpdate(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None
