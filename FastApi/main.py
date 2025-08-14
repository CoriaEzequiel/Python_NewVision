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
    },
    {
        "id":2,
        "title": "Batman",
        "overview": "Sumergete en las profundidades de Gotham City",
        "year":"1989",
        "rating": 8.2,
        "category": "Acción"
    }
]


#@app.get('/', tags=['Home']) #añado atributos al endpoint (con tags agrupo endpoints)
#def home():
#    return "Welcome" #respuesta string


@app.get('/movies', tags=['Home'])
def get_movies():
    return movies
   # return {"Hello":"world"} #respuesta diccionario
   # return HTMLResponse('<h1>List of movies</h1>') #html response
    

#PARAMETROS DE RUTA: valores que puedo pasar dentro de la URL
@app.get('/movies/{id}', tags=['Home'])
def get_movie(id:int):                   # para imprimir el valor id debemos indicarlo también dentro de la f(añadirlo como parámetro)
    for movie in movies:
        if movie['id'] == id:
            return movie
    return[]



@app.get('/movies/', tags=['Home'])       #ya no filtro por id (/movies/ esta va tener parámetros query)
def get_movie_by_category(category:str, year:int):      # defino param por query, es añadiendo dentro de la f()
             
    for movie in movies:
        if movie['category'] == category:
            return movie
    return[]