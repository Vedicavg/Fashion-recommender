from flask import Flask, request, jsonify
import pickle
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.models import Sequential
from numpy.linalg import norm
from sklearn.neighbors import NearestNeighbors
import os
import io

# Load precomputed features and file paths
features_list = pickle.load(open("image_features_embedding.pkl", "rb"))
img_files_list = pickle.load(open("img_files.pkl", "rb"))

# Initialize ResNet50 model
model = ResNet50(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
model.trainable = False
model = Sequential([model, GlobalMaxPooling2D()])

# Initialize Flask application
app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    image_file = request.files['image']

    # Convert SpooledTemporaryFile to BytesIO
    image_stream = io.BytesIO(image_file.stream.read())

    # Load the image using keras.preprocessing.image.load_img
    img = image.load_img(image_stream, target_size=(224, 224))
    img_array = image.img_to_array(img)
    expand_img = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expand_img)
    
    # Extract features using your model
    result_to_resnet = model.predict(preprocessed_img)
    flatten_result = result_to_resnet.flatten()
    result_normalized = flatten_result / norm(flatten_result)
    
    # Perform nearest neighbor search
    neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
    neighbors.fit(features_list)
    distances, indices = neighbors.kneighbors([result_normalized])
    
    # Prepare response with file paths
    similar_images = []
    for file_idx in indices[0][1:6]:
        similar_images.append(img_files_list[file_idx])
    
    return jsonify({'similar_images': similar_images})

if __name__ == '__main__':
    app.run(debug=True)
