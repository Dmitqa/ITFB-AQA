from pydantic import BaseModel


class Dog(BaseModel):
    message: list
    status: str

