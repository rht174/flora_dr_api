import werkzeug
from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.applications.mobilenet_v2 import decode_predictions

app = Flask(__name__)

plant_dict = {'apple': 'Apple', 'corn': 'Corn', 'grape': 'Grape', 'tea': 'Tea', 'tomato': 'Tomato'}

classes_dict = {'apple': ['Scab', 'Black Rot', 'Cedar Apple Rust', 'Healthy'],
                'corn': ['Blight', 'Common Rust', 'Gray Leaf Spot', 'Healthy'],
                'grape': ['Black Rot', 'Black Measles', 'Healthy', 'Leaf Blight Isariopsis Leaf Spot'],
                'tea': ['Bird Eye Spot', 'Brown Blight', 'Healthy', 'Red Leaf Spot'],
                'tomato': ['Late Blight', 'Bacterial Spot', 'Early Blight', 'Healthy']}


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def prediction():
    if request.method == 'POST':
        imagefile = request.files['image']
        temp_path = 'temp/temp_image.jpg'
        imagefile.save(temp_path)
        plant = request.form['plant']

        model = keras.models.load_model(f'models/{plant}.h5')
        img = tf.keras.preprocessing.image.load_img(temp_path, target_size=(224, 224))
        img = tf.keras.utils.img_to_array(img)
        img = img / 255
        img = np.array([img])
        pred = model.predict(img)
        condition = np.argmax(pred)
        confidence = round(100 * (np.max(pred)), 2)

        health = classes_dict[plant][condition]

        return render_template('index.html', plant_name=plant_dict[plant], plant_condition=health,
                               pred_confidence=confidence)


if __name__ == "__main__":
    app.run(debug=True)
