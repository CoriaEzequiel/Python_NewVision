from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()  # instancia de FastAPI

# DATA
# Lista en memoria(actuando como base de datos temporal)
movies = [
    {"id":1, "title": "Avatar", "overview": "Aventuras en Pandora", "year":2009, "rating": 7.9, "category": "Ficción"},
    {"id":2, "title": "Batman", "overview": "Sumergete en las profundidades de Gotham City", "year":1989, "rating": 8.2, "category": "Acción"}
]

# MODELS
class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    overview: Optional[str] = None
    year: Optional[int] = None
    rating: Optional[float] = None
    category: Optional[str] = None


@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies #Devuelve todas las películas

@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int): 
   
    for movie in movies:
        if movie["id"] == id:    #Devuelve una película por id
            return movie
    return []

@app.get("/movies/filter", tags=["Movies"])
def get_movie_by_category(category: str = None, year: int = None):
    # Filtrado por query params opcionales
    results = movies
    if category:
        results = [m for m in results if m["category"] == category]
    if year:
        results = [m for m in results if m["year"] == year]
    return results


@app.post("/movies", tags=["Movies"])
def create_movie(movie: Movie):
    # Crea una nueva película usando Pydantic
    movies.append(movie.dict())
    return movies


@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie_data: MovieUpdate):
    # Actualiza solo los campos enviados
    for movie in movies:
        if movie["id"] == id:
            update_data = movie_data.dict(exclude_unset=True)
            movie.update(update_data)
            return movie
    return {"error": "Movie not found"}


@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    # Elimina película por id
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return movies
    return {"error": "Movie not found"}
