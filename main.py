import werkzeug
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def prediction():
    if request.method == 'POST':
        imagefile = request.files['image']
        return jsonify({'message': 'image received successfully'})


if __name__ == "__main__":
    app.run(debug=True, port=4000)
