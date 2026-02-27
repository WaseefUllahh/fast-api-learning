from fastapi import FastAPI  # import
from typing import Optional
from pydantic import BaseModel
# import uvicorn

app = FastAPI()  # this creates an instance of the FastAPI class, which is the main entry point for creating a FastAPI application. It allows you to define routes, handle requests, and manage the overall behavior of your API.


@app.get(
    "/"
)  # ("/") this is path .what does this do? it creates an endpoint at the root of the API that listens for GET requests. When a GET request is made to this endpoint, the function index() will be executed.
def index():  # function
    return {"data": "blog list"}  # msg to return when the endpoint is hit


@app.get(
    "/blog"
)  # this is the endpoint for getting all published blogs. when a GET request is made to this endpoint, the function published() will be executed and it will return a JSON response with the message "all published blogs".
def index2(limit=10, published: bool = True, sort: Optional[str] = None):  #
    if published:
        return {"data": f"{limit} published blogs"}
    else:
        return {"data": f"{limit} blogs from database"}


@app.get(
    "/blog/unpublished"
)  # this is the endpoint for getting all unpublished blogs. when a GET request is made to this endpoint, the function unpublished() will be executed and it will return a JSON response with the message "all unpublished blogs".
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get(
    "/blog/{id}"
)  #  .get is a decorator that tells FastAPI that this function should be called when a GET request is made to the "/about" endpoint. When a GET request is made to this endpoint, the function about() will be executed.
def show(
    id: int,
):  # here i have defined the type for parameter id and int. so it will only accept integer value for id and if we try to pass string value it will give error. this is one of the main features of fastapi that it has built in validation for request parameters.
    return {
        "data": id
    }  # path operation function that returns a JSON response with the message "about page" when the "/about" endpoint is accessed via a GET request.


# example : {
#   "data": 123
# }

# for dynamic id we can use {variable_name} in path and then transfer it to function and use it and return it in response.
# @app is a decorator that tells FastAPI that the function below it should be associated with a specific HTTP method and path. In this case, @app.get("/") means that the index() function will be called when a GET request is made to the root path ("/") of the API.


@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    # fetch comments of a blog with id = id
    return {
        "data": {
            1,
            2,
        }
    }


# we have to take good care when creating dynamic endpoints because if we have two endpoints like /blog/{id} and /blog/unpublished then when we try to access /blog/unpublished it will give error because it will try to match it with /blog/{id} and it will not find
# any integer value for id and it will give error. so we have to make sure that we are not creating conflicting endpoints.


class Blog(BaseModel):  # this is the model the blog model.
    title: str
    body: str
    published: Optional[bool]


# we use that  blog model in here and get the values from user to api.
@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"Blog is created with  title as {blog.title}"}


# HOW TO DEBUG. we add a breakpoint applicationo will stop at that point and we can then debug.

# How to chnage the port from default port:
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
