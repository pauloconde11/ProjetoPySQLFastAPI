from fastapi import FastAPI, Depends, HTTPException
import services, models, schemas
from db import get_db, engine
from sqlalchemy.orm import Session
from typing import List  

app = FastAPI()

@app.get("/books/", response_model=List[schemas.BookResponse])  
def get_all_books(db: Session = Depends(get_db)):
    return services.get_books(db)  

@app.get("/books/{book_id}", response_model=schemas.Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book_queryset = services.get_books(db, book_id)
    if book_queryset:
        return book_queryset
    raise HTTPException(status_code=404, detail="Invalid book id provided")

@app.post("/books/", response_model=schemas.BookResponse) 
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db) ):
    return services.create_book(db, book)

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book: schemas.BookCreate, book_id: int, db: Session = Depends(get_db)):
    db_update = services.update_book(db, book, book_id)  
    if not db_update:
        raise HTTPException(status_code=404, detail="book not found")
    return db_update

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    delete_entry = services.delete_book(db, book_id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail="book not found")

