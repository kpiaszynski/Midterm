from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    title: str
    desc: str
    rating: int | None = None  # Initialize as None


class MovieRequest(BaseModel):
    title: str
    desc: str
    rating: int | None = None  # Initialize as None
