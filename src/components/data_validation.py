import os
import sys
from src.exception import CustomException
from src.logger import logging as lg
import pandas as pd

class DataValidation:
    def __init__(self, raw_data_store_dir):
        self.raw_data_store_dir = raw_data_store_dir
        self.valid_data_dir = "valid_data"
        os.makedirs(self.valid_data_dir, exist_ok=True)

    def validate_data(self, df):
        try:
            # Check for required columns
            required_columns = ['target']  # Add other required columns
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise CustomException(f"Missing required columns: {missing_columns}", sys)
            
            # Check for null values
            null_counts = df.isnull().sum()
            if null_counts.any():
                lg.warning(f"Found null values in columns: {null_counts[null_counts > 0]}")
            
            # Remove rows with null values
            df = df.dropna()
            
            return df
            
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_validation(self):
        try:
            # Read raw data
            raw_data_path = os.path.join(self.raw_data_store_dir, "raw_data.csv")
            df = pd.read_csv(raw_data_path)
            
            # Validate data
            df = self.validate_data(df)
            
            # Save validated data
            valid_data_path = os.path.join(self.valid_data_dir, "valid_data.csv")
            df.to_csv(valid_data_path, index=False)
            
            lg.info("Data validation completed successfully")
            return self.valid_data_dir
            
        except Exception as e:
            raise CustomException(e, sys) 