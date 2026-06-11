from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CONFIGURACIÓN BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

# MODELO
class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    programa = db.Column(db.String(50), nullable=False)
    fecha_inscripcion = db.Column(db.DateTime, default=db.func.now())

# RUTAS
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/informacion")
def informacion():
    return render_template("informacion.html", objetivos=objetivos)

@app.route("/recursos")
def recursos():
    return render_template("recursos.html", enlaces=enlaces)

@app.route("/tareas")
def tareas_pagina():
    return render_template("tareas.html", tareas=tareas)

@app.route("/inscripcion", methods=["GET", "POST"])
def inscripcion():
    mensaje = None

    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        programa = request.form.get("programa")

        if not nombre or not email or not programa:
            mensaje = "Por favor completa todos los campos."
        else:
            try:
                nuevo = Estudiante(
                    nombre=nombre,
                    email=email,
                    programa=programa
                )
                db.session.add(nuevo)
                db.session.commit()
                mensaje = f"Bienvenido {nombre}! Te hemos registrado."
            except:
                db.session.rollback()
                mensaje = "Error: este email ya está registrado."

    return render_template("inscripcion.html", mensaje=mensaje)


@app.route("/estudiantes")
def estudiantes():
    lista = Estudiante.query.all()
    return render_template("estudiantes.html", estudiantes=lista)


if __name__ == "__main__":
    app.run(debug=True)