
from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


# Define a route to handle the image classification
@app.route('/classify', methods=['POST'])
def classify_image():
    # Handle the image classification logic here
    # You'll need to extract the image from the request and use TensorFlow.js and Teachable Machine to classify it
    
    # Placeholder response for now
    response = {
        'label': 'apple',
        'confidence': 0.95,
        'details': {
            'nutritional_value': '...',
            'origin': '...',
            'seasonality': '...'
        }
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
