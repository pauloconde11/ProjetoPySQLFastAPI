from models import Book
from sqlalchemy.orm import Session
from schemas import BookCreate

# Criar um novo livro
def create_book(db: Session, data: BookCreate):
    book_instance = Book(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance

# Obter todos os livros ou um livro específico
def get_books(db: Session, book_id: int = None):
    if book_id:
        return db.query(Book).filter(Book.id == book_id).first()
    return db.query(Book).all()

# Atualizar um livro existente
def update_book(db: Session, book: BookCreate, book_id: int):
    book_queryset = db.query(Book).filter(Book.id == book_id).first()
    if book_queryset:
        for key, value in book.model_dump().items():
            setattr(book_queryset, key, value)
        db.commit()
        db.refresh(book_queryset)
    return book_queryset

# Excluir um livro
def delete_book(db: Session, book_id: int):
    book_queryset = db.query(Book).filter(Book.id == book_id).first()
    if book_queryset:
        db.delete(book_queryset)
        db.commit()
    return book_queryset
