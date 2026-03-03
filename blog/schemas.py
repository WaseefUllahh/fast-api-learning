from pydantic import BaseModel


# Schemas are for the user (API)
class Blog(BaseModel):
    title: str
    body: str
