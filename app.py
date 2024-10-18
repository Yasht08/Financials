from flask import Flask, request, jsonify
import json
import model  # Import your model.py file
from flask_cors import CORS  # Import CORS to handle cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Financial Analysis API!"})

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the file part is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    # If the user did not select a file, the browser submits an empty file
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        # Load the JSON data from the uploaded file
        data = json.load(file)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON file"}), 400

    # Process the uploaded data using model.py
    results = model.probe_model_5l_profit(data["data"])
    
    # Return the results as JSON
    return jsonify(results)

if __name__ == '__main__':
    # Start the Flask app with debug mode enabled
    app.run(debug=True)
