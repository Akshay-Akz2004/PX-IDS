import os
from dotenv import load_dotenv
from pymongo import MongoClient
from src.logger import logging as lg

# Load environment variables
load_dotenv()

def test_mongo_connection():
    try:
        # Get MongoDB URI and database name
        mongo_url = os.getenv("MONGO_URL")
        db_name = os.getenv("DATABASE_NAME")
        
        print(f"Environment variables loaded:")
        print(f"MONGO_URL: {mongo_url}")
        print(f"DATABASE_NAME: {db_name}")
        
        if not mongo_url:
            print("Error: MONGO_URL is not set in .env file")
            return False
            
        if not db_name:
            print("Error: DATABASE_NAME is not set in .env file")
            return False
        
        # Test connection
        print("\nAttempting to connect to MongoDB...")
        client = MongoClient(mongo_url)
        db = client[db_name]
        
        # List collections to verify connection
        collections = db.list_collection_names()
        print(f"\nSuccessfully connected to MongoDB!")
        print(f"Available collections: {collections}")
        
        return True
    except Exception as e:
        print(f"\nError connecting to MongoDB: {str(e)}")
        return False

if __name__ == "__main__":
    print("Starting MongoDB connection test...")
    test_mongo_connection() 