from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() #instancia de FastAPI

#app.title = "Hi"
#app.version = "2.0.0"

movies = [          #lista de diccionarios
    {
        "id":1,
        "title": "Avatar",
        "overview": "Aventuras en Pandora",
        "year":"2009",
        "rating": 7.9,
        "category": "Ficción"
    }
]


@app.get('/', tags=['Home']) #añado atributos al endpoint (con tags agrupo endpoints)
def home():
    return "Welcome" #respuesta string


@app.get('/movies', tags=['Home'])
def home():
    return movies
   # return {"Hello":"world"} #respuesta diccionario
   # return HTMLResponse('<h1>List of movies</h1>') #html response
    
