from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"]) #Flask acepta solicitudes GET y POST para esta ruta.
def home_form():
    info_formulario= ""
    if request.method =="POST": #si app recibe info
        info_formulario = request.form.get("contenido") #guardo en un formulario indicando desde qué input lo obtengo.
        print(f"Holamigo {info_formulario}")
    return render_template("formulario.html", nombre = info_formulario)

if __name__ == "__main__":
    app.run(debug=True)