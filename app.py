from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)

plant_dict = {'apple': 'Apple', 'corn': 'Corn', 'grape': 'Grape', 'tea': 'Tea', 'tomato': 'Tomato'}

classes_dict = {'apple': ['Scab', 'Black Rot', 'Cedar Apple Rust', 'Healthy'],
                'corn': ['Blight', 'Common Rust', 'Gray Leaf Spot', 'Healthy'],
                'grape': ['Black Rot', 'Black Measles', 'Blight Isariopsis Leaf Spot', 'Healthy'],
                'tea': ['Bird Eye Spot', 'Brown Blight', 'Healthy', 'Red Leaf Spot'],
                'tomato': ['Late Blight', 'Bacterial Spot', 'Early Blight', 'Healthy']}

plant_name = None
health = None
confidence = None


# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def prediction():
    global plant_name, health, confidence

    if request.method == 'POST':
        imagefile = request.files['image']
        temp_path = 'temp/temp_image.jpg'
        imagefile.save(temp_path)
        # plant = request.form['plant']
        x = request.values
        plant = x['plant']
        # request_data = request.data
        # request_data = json.loads(request_data.decode('utf-8'))
        # plant = request_data['plant']

        model = keras.models.load_model(f'models/{plant}.h5')
        img = tf.keras.preprocessing.image.load_img(temp_path, target_size=(224, 224))
        img = tf.keras.utils.img_to_array(img)
        img = img / 255
        img = np.expand_dims(img, axis=0)
        pred = model.predict(img)
        condition = np.argmax(pred)
        plant_name = plant_dict[plant]
        health = classes_dict[plant][condition]
        confidence = str(round(100 * (np.max(pred)), 2))
        print(plant_name, health, confidence)

        return ''

    else:
        return jsonify({'plant': plant_name, 'health': health, 'confidence': confidence})

        # return render_template('index.html', plant_name=plant_dict[plant], plant_condition=health,
        #                        pred_confidence=confidence)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
