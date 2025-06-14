import os
import sys
from src.exception import CustomException
from src.logger import logging as lg
import pandas as pd
from src.data_access.mongo_db import MongoDBClient

class DataIngestion:
    def __init__(self):
        self.mongo_client = MongoDBClient()
        self.raw_data_dir = "raw_data"
        os.makedirs(self.raw_data_dir, exist_ok=True)

    def initiate_data_ingestion(self):
        try:
            # Get data from MongoDB
            collection = self.mongo_client.get_collection('phishing_data')
            data = list(collection.find({}, {'_id': 0}))
            df = pd.DataFrame(data)
            
            # Save raw data
            raw_data_path = os.path.join(self.raw_data_dir, "raw_data.csv")
            df.to_csv(raw_data_path, index=False)
            
            lg.info("Data ingestion completed successfully")
            return self.raw_data_dir
            
        except Exception as e:
            raise CustomException(e, sys) 