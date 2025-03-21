from pydantic import BaseModel


class Books(BaseModel):
    title: str
    author: str
    pages: str
    genre: str


class Reference(BaseModel):
    name: str
    gender: str
    address: str
    age: int
    books: list[Books] = []
