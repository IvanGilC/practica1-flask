# importamos las funciones necesarias de flask
# Flask sirve para crear la aplicacion web
# render_template sirve para mostrar paginas html
# request sirve para leer datos enviados desde formularios
from flask import Flask, render_template, request

# importamos funciones del archivo database
# init_db inicializa la base de datos
# guardar_grup guarda un grupo de nombres
# carregar_grup carga el grupo guardado
from database import init_db, guardar_grup, carregar_grup

# creamos la aplicacion flask
app = Flask(__name__)

# inicializamos la base de datos al arrancar la aplicacion
init_db()

# definimos la ruta principal "/"
# acepta peticiones GET y POST
@app.route("/", methods=["GET", "POST"])
def index():

    # si la peticion es POST significa que el usuario ha enviado el formulario
    if request.method == "POST":

        # obtenemos el texto del campo "noms" del formulario
        noms_text = request.form.get("noms")

        # si hay texto en el formulario
        if noms_text:

            # separamos los nombres por comas
            # strip elimina espacios antes y despues de cada nombre
            grup = [nom.strip() for nom in noms_text.split(",")]

            # guardamos el grupo en la base de datos
            guardar_grup(grup)

    # cargamos el grupo guardado en la base de datos
    grup = carregar_grup()

    # mostramos la plantilla index.html y le pasamos el grupo de nombres
    return render_template("index.html", grup=grup)


# si este archivo se ejecuta directamente
if __name__ == "__main__":

    # iniciamos el servidor web
    # host 0.0.0.0 permite acceder desde otras maquinas
    # port 8000 es el puerto donde se ejecuta
    # debug False desactiva el modo depuracion
    app.run(host="0.0.0.0", port=8000, debug=False)