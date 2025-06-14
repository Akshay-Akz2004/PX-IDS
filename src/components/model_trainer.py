import os
import sys
from src.exception import CustomException
from src.logger import logging as lg
import numpy as np
from xgboost import XGBClassifier
from src.utils import save_object

class ModelTrainer:
    def __init__(self):
        self.model_path = os.path.join('artifacts', 'model.pkl')

    def initiate_model_trainer(self, x_train, y_train, x_test, y_test, preprocessor_path):
        try:
            # Initialize and train the model
            model = XGBClassifier(
                n_estimators=100,
                learning_rate=0.1,
                max_depth=5,
                random_state=42
            )
            
            model.fit(x_train, y_train)
            
            # Save the model
            save_object(self.model_path, model)
            
            # Calculate and log scores
            train_score = model.score(x_train, y_train)
            test_score = model.score(x_test, y_test)
            
            lg.info(f"Model training completed. Train score: {train_score:.4f}, Test score: {test_score:.4f}")
            
            return test_score
            
        except Exception as e:
            raise CustomException(e, sys) 