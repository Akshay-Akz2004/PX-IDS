import os
import sys
from src.exception import CustomException
from src.logger import logging as lg
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from src.utils import save_object

class DataTransformation:
    def __init__(self, valid_data_dir):
        self.valid_data_dir = valid_data_dir
        self.preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

    def initiate_data_transformation(self):
        try:
            # Read validated data
            valid_data_path = os.path.join(self.valid_data_dir, "valid_data.csv")
            df = pd.read_csv(valid_data_path)
            
            # Split features and target
            X = df.drop('target', axis=1)
            y = df['target']
            
            # Split into train and test
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Scale the features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            # Save the preprocessor
            save_object(self.preprocessor_path, scaler)
            
            lg.info("Data transformation completed successfully")
            
            return X_train_scaled, y_train, X_test_scaled, y_test, self.preprocessor_path
            
        except Exception as e:
            raise CustomException(e, sys) 