from fastapi import FastAPI
from . import schemas

app = FastAPI()


# CRUD Operation:
@app.post("/blog")  # to create a blog
def create(request: schemas.Blog):  #
    return request
