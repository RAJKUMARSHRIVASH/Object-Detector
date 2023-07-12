# import os
# from flask import Flask, jsonify, request, send_from_directory, render_template
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route("/")
# def home():
#     return render_template('index.html')


# @app.route('/api/detect-object', methods=['POST'])
# def detect_object():
#     # Check if the image file is present in the request
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image file provided'}), 400

#     image_file = request.files['image']

#     # Check if the file has an allowed extension
#     if image_file and allowed_file(image_file.filename):
#         filename = secure_filename(image_file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         image_file.save(filepath)

#         # TODO: Perform object detection using the saved image file

#         # TODO: Return the detection results as JSON response

#         return jsonify({'result': 'Detection result'})
#     else:
#         return jsonify({'error': 'Invalid file extension'}), 400


# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# if __name__ == '__main__':
#     app.run(debug=True)


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
    app.run(debug=True)
