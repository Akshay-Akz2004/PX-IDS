import os
from src.logger import logging

# AWS S3 bucket name
AWS_S3_BUCKET_NAME = "phishing-detection-model"

# Target column name
TARGET_COLUMN = "prediction"

# Model artifacts directory
MODEL_ARTIFACTS_DIR = "artifacts"

# Prediction artifacts directory
PREDICTION_ARTIFACTS_DIR = "prediction_artifacts"

# Predictions directory
PREDICTIONS_DIR = "predictions"

# Logs directory
LOGS_DIR = "logs"

# Create necessary directories
os.makedirs(MODEL_ARTIFACTS_DIR, exist_ok=True)
os.makedirs(PREDICTION_ARTIFACTS_DIR, exist_ok=True)
os.makedirs(PREDICTIONS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

logging.info("Constants initialized and directories created.")