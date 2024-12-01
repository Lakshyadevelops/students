from typing import Optional
from pydantic import BaseModel


def StudentEntityOnlyID(item) -> dict:
    return {
        "id": str(item.inserted_id),
    }


def studentEntity(item) -> dict:
    return {
        "name": item["name"],
        "age": item["age"],
        "address": item["address"],
    }


def studentEntityWithOutAddress(item) -> dict:
    return {
        "name": item["name"],
        "age": item["age"],
    }


def studentsEntityWithOutAddress(entity) -> list[dict]:
    return [studentEntityWithOutAddress(item) for item in entity]
