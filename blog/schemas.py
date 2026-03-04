from pydantic import BaseModel


# Schemas are for the user (API)
class Blog(BaseModel):
    title: str
    body: str


class ShowBlog(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True

    pass
