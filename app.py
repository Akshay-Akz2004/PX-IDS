from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
import os, sys
from dotenv import load_dotenv

from src.pipeline.train_pipeline import TrainingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainingPipeline()
        scores = train_pipeline.run_pipeline()
        
        return jsonify({
            "status": "success",
            "message": "Training Completed Successfully",
            "scores": scores
        })
    except Exception as e:
        lg.error(f"Training failed: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                return jsonify({
                    "status": "error",
                    "message": "No file uploaded"
                }), 400
                
            prediction_pipeline = PredictionPipeline(request)
            prediction_file_detail = prediction_pipeline.run_pipeline()
            
            lg.info("Prediction completed. Downloading prediction file.")
            return send_file(
                prediction_file_detail.prediction_file_path,
                download_name=prediction_file_detail.prediction_file_name,
                as_attachment=True
            )
        else:
            return render_template('prediction.html')
    except Exception as e:
        lg.error(f"Prediction failed: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    # Create necessary directories
    os.makedirs('artifacts', exist_ok=True)
    os.makedirs('predictions', exist_ok=True)
    os.makedirs('prediction_artifacts', exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    
    app.run(host="0.0.0.0", port=8080, debug=True)
