from pydantic import BaseModel

# Modelo base (herda de BaseModel)
class BookBase(BaseModel):
    title: str
    description: str
    author: str
    year: int

# Modelo de entrada (para criação de um novo livro)
class BookCreate(BookBase):
    pass

# Modelo de saída (para resposta da API)
class BookResponse(BaseModel):
    id: int
    title: str
    author: str

    class Config:
        from_attributes = True  # pydantic v2 (substitui orm_mode)

# Modelo completo (inclui o ID)
class Book(BookBase):
    id: int

    class Config:
        from_attributes = True  # pydantic v2 (substitui orm_mode)