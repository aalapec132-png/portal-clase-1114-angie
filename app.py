from flask import Flask, render_template

app = Flask(__name__)

# Datos de la clase
objetivos = [
    "Aprender Python",
    "Aprender Flask",
    "Crear aplicaciones web"
]

tareas = [
    {"numero": 1, "titulo": "Instalar Python", "fecha": "2026-06-01"},
    {"numero": 2, "titulo": "Crear entorno virtual", "fecha": "2026-06-02"},
    {"numero": 3, "titulo": "Aprender Flask", "fecha": "2026-06-03"}
]

enlaces = [
    {"nombre": "Documentacion Flask", "url": "https://flask.palletsprojects.com"},
    {"nombre": "Tutorial Python", "url": "https://docs.python.org"},
    {"nombre": "GitHub del Profesor", "url": "https://github.com/hortegon"},
    {"nombre": "MDN - HTML y CSS", "url": "https://developer.mozilla.org"}
]

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/informacion")
def informacion():
    return render_template(
        "informacion.html",
        objetivos=objetivos
    )

@app.route("/recursos")
def recursos():
    return render_template(
        "recursos.html",
        enlaces=enlaces
    )

@app.route("/tareas")
def tareas_pagina():
    return render_template(
        "tareas.html",
        tareas=tareas
    )

if __name__ == "__main__":
    app.run(debug=True)