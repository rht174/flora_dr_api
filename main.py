import werkzeug
from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.applications.mobilenet_v2 import decode_predictions

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def prediction():
    if request.method == 'POST':
        imagefile = request.files['image']
        temp_path = 'temp/temp_image.jpg'
        imagefile.save(temp_path)
        # return jsonify({'message': 'image received successfully'})

        model = keras.models.load_model('models/apple.h5')

        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
