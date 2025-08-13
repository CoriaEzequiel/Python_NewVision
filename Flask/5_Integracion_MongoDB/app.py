from flask import Flask, render_template, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Cargo variables de entorno
load_dotenv()


app = Flask(__name__)

# Leo MONGO_URI desde .env
mongo_uri = os.getenv("MONGO_URI")                              
cliente = MongoClient(mongo_uri)    #creo un cliente mongo
app.db = cliente.lista_users
usuarios = [usuario for usuario in app.db.usuarios.find({})] #recorrido dentro de la dB en mongo
print(usuarios)
@app.route("/", methods = ["GET", "POST"]) #dentro de la app (rout) donde estaré utilizando get y post (al ingresar a la raíz o al recibir información del formulario)
def home():
    if request.method =="POST": #si app recibe info del form (que viene del imput contenido)
        info_formulario = request.form.get("contenido") 
        parametros={"nombre":info_formulario}   #guardo lista de Diccionarios != a la lista de elementos
        usuarios.append(parametros) 
        app.db.usuarios.insert_one(parametros)
    return render_template("formulario.html", usuarios = usuarios) #variable usuarios en form.

if __name__ == "__main__":
    app.run(debug=True)