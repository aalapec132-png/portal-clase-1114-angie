from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():

 nombre_profesor = "Prof. Henry - Kyrbot Innovations" 
 email = "henry@kyrbot.com" 
 horario = "Lunes a Viernes - 7:00 PM"
 aula = "Aula Virtual Flask 1114"
 descripcion = "Portal de aprendizaje Flask con Python y HTML"


 return render_template( 
"index.html",
 nombre_profesor=nombre_profesor,
email=email, 
horario=horario,
aula=aula,
descripcion=descripcion
)

if __name__ == "__main__": 
   app.run(debug=True)