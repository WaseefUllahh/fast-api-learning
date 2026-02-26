from fastapi import FastAPI  # import

app = FastAPI()  # this creates an instance of the FastAPI class, which is the main entry point for creating a FastAPI application. It allows you to define routes, handle requests, and manage the overall behavior of your API.


@app.get(
    "/"
)  # what does this do? it creates an endpoint at the root of the API that listens for GET requests. When a GET request is made to this endpoint, the function index() will be executed.
def index():  # function
    return {"data": {"name": "Waseef Ullah"}}  # msg to return when the endpoint is hit


@app.get("/about")
def about():
    return {"data": "about page"}
