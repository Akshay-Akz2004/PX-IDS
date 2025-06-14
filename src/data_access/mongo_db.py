import os
import sys
from src.exception import CustomException
from src.logger import logging as lg
from pymongo import MongoClient
from dotenv import load_dotenv

class MongoDBClient:
    def __init__(self):
        try:
            # Load environment variables
            load_dotenv()
            
            # Get MongoDB connection details from environment variables
            self.mongo_url = os.getenv('MONGO_URL')
            self.database_name = os.getenv('DATABASE_NAME')
            
            if not self.mongo_url or not self.database_name:
                raise CustomException("MongoDB configuration not found in environment variables", sys)
            
            # Create MongoDB client
            self.client = MongoClient(self.mongo_url)
            self.database = self.client[self.database_name]
            
            # Test the connection
            self.test_connection()
            
            lg.info("MongoDB connection established successfully")
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def test_connection(self):
        try:
            # Ping the server to verify connection
            self.client.admin.command('ping')
            lg.info("Successfully connected to MongoDB")
        except Exception as e:
            lg.error(f"Failed to connect to MongoDB: {str(e)}")
            raise CustomException("Failed to connect to MongoDB", sys)
    
    def get_collection(self, collection_name):
        try:
            return self.database[collection_name]
        except Exception as e:
            raise CustomException(e, sys)
    
    def insert_many(self, collection_name, documents):
        try:
            collection = self.get_collection(collection_name)
            result = collection.insert_many(documents)
            return result.inserted_ids
        except Exception as e:
            raise CustomException(e, sys)
    
    def find_all(self, collection_name, query=None):
        try:
            collection = self.get_collection(collection_name)
            if query is None:
                query = {}
            return list(collection.find(query))
        except Exception as e:
            raise CustomException(e, sys)
    
    def close(self):
        try:
            self.client.close()
            lg.info("MongoDB connection closed successfully")
        except Exception as e:
            raise CustomException(e, sys) 