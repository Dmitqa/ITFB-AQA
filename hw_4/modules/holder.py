from pydantic import BaseModel, field_validator, PydanticUserError


class Holder(BaseModel):
    userId: int
    id: int
    title: str
    body: str

    @field_validator("title")
    def title_check(cls, title):
        if title:
            return title
        else:
            raise PydanticUserError("Empty title!")
