# Importar los módulos necesarios.
from flask import Flask , render_template , request , jsonify

# Importar el archivo de análisis de sentimiento sentiment_analysis como sa
import sentiment_analysis as sa

app = Flask(__name__)

# Ruta de la app para la página index.
@app.route('/')
def home():
    return render_template('index.html')

# Escribir una ruta para el requerimiento POST.
@app.route('/predict-emotion', methods=["POST"])
def review():

    # Extraer la reseña del cliente (customer_review) escribiendo la 'clave' apropiada de los datos JSON.
    review = request.json.get('')

    # Comprobar si customer_review está vacía, devolver el error.
    if not review:

        return jsonify({'status' : 'error' , 
                        'message' : 'Reseña vacía'})

    # Si la reseña no está vacía, pasarla por la función 'predict' - (predecir).
    # La función predict devuelve 2 cosas: la emoción y la ruta de la imagen en la carpeta static.
    # Ejemplo: Positivo , ./static/assets/emoticons/positive.png

    else:

        _ , _ = sa.predict(review)

        return jsonify({'':'' , '':''})


if __name__  ==  "__main__":
    app.run(debug = True)