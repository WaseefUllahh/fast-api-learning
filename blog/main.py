from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CRUD Operation:
@app.post("/blog", status_code=status.HTTP_201_CREATED)  # to create a blog
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete(
    "/blog/{id}", status_code=status.HTTP_204_NO_CONTENT
)  # For Deleting a Blog.
def destroy(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id)  # blog query
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():  # if blog is not available
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    blog.delete(synchronize_session=False)  # if blog is available
    db.commit()  # to save changes to database and update it.
    return "done"


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    blog.update(
        request.dict()
    )  # normal request was not working here so I am using th dictionary. because it take request as a dictionary form.
    db.commit()
    return "updated successfully"


@app.get(
    "/blog", response_model=List[schemas.ShowBlog]
)  # As we are getting collection of blogs so we will convert it to list.
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = (
        db.query(models.Blog).filter(models.Blog.id == id).first()
    )  # we are using sqlalchemy orm
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with the id {id} is not available"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} not found",
        )
    return blog
