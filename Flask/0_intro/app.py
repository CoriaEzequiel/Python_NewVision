from flask import Flask, render_template

#instancia de Flask, instancia de mi app

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

#defino ruta en app flask
@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/elegant")
def elegant_hello_world():
    return """
            <html>
                <body>
                    <h1>Hello</h1>
                    <p>World </p>
                </body>
            </html>
           """

#asocio templates

@app.route("/first")
def first_template():
    return render_template("first_site.html")

@app.route("/second")
def second_site():
    return render_template("second_site.html")

# un mismo template puede utilizarse para varios contenidos

@app.route("/with_variables")
def welcome_():
    return render_template("variable_template.html", name= "Ezequielcito", my_class="Python")

#mismo template con distintos parámetros
@app.route("/with_new_variable")
def welcome_new():
    return render_template("variable_template.html", name= "Ez", my_class="Python")


@app.route("/expressions")
def expressions():
    name = "Ezequiel"
    last_name="Coria"
    color = "Light Blue"
    base = 5
    altura = 10
    return render_template("expressions.html", name = name, last_name = last_name, color= color, base= base, altura=altura )

@app.route("/expressions2")
def expressions2():  
    kwargs = {      #entrego diccionario kwargs (key/value)
    "name":"Ez",
    "last_name":"Coria",
    "color": "Red",
    "base": 2,
    "altura":7
    }
    return render_template(template_name_or_list="expressions.html", **kwargs) #**entrega diccionario



if __name__ == "__main__":
    app.run(debug=True)