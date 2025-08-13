from flask import Flask, render_template

app= Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True 
class Pelicula:                        #entrego clase
    def __init__(self,nombre, anio, protagonista):
        self.nombre = nombre
        self.anio = anio
        self.protagonista = protagonista



@app.route("/estructura")
def estructura_datos():
    peliculas = [                       #entrego lista(Array) de películas. (elemento[0],[1]...)
        "El lobo de Wall Street",
        "Harry Potter",
        "Volver al Futuro"
    ]
    #return render_template("estructuras.html", movies= peliculas)


    lobo = {                            #entrego diccionario
    "Nombre": "El lobo de Wall Street",
    "anio": 2013,
    "Protagonista": "Leo DiCaprio"
    }

 #   return render_template(template_name_or_list="estructuras.html",
 #                     movies=peliculas, destacada=lobo) 

 # utilizo la clase Pelicula

    backto = Pelicula(nombre='Volver al Futuro',anio="1985",protagonista="Michael J. Fox")

                        
    return render_template(template_name_or_list="estructuras.html",   #parámetros que paso a mi render
                       movies=peliculas, destacada=lobo, favorita=backto) 


if __name__ == "__main__":
    app.run(debug=True)