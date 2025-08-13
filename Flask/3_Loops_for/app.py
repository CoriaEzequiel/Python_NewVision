from flask import Flask, render_template

app = Flask(__name__)


@app.route("/for-loop") #ruta donde se ejecuta la función
def loop_for():
    equipos= [
        "Real Madrid",
        "Barcelona Fc",
        "Milan Ac",
        "Liverpool",
        "Bayern Munich",
        "Ajax Amsterd",
        "Inter Milan",
        "Juventus",
        "Manchester United",
        "Oporto"
    ]

    equipo_champ = {
        "Real Madrid":14,
        "Milan Ac":7,
        "Liverpool":6,
        "Bayern Munich":5,
        "Barcelona":5,
        "Ajax Amsterd":4,
        "Inter Milan":3,
        "Manchester United":3
    }

    return render_template("for_loop.html", teams = equipos, teams_dic = equipo_champ)




if __name__ == "__main__":
    app.run(debug=True)