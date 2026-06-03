from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/informacion")
def informacion():
    return render_template("informacion.html")

@app.route("/recursos")
def recursos():
    return render_template("recursos.html")

@app.route("/tareas")
def tareas():
    return render_template("tareas.html")

if __name__ == "__main__":
    app.run(debug=True)
    0