from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

uri = os.getenv("MONGODB_URI")

if not uri:
    print("MONGODB_URI not found in .env file.")
    exit(1)

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    exit(1)

csv_path = os.path.join(os.path.dirname(__file__), "phishing.csv")

try:
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} records from CSV.")
    print(df.head())  # Show first few rows for verification
except Exception as e:
    print(f"Error reading CSV file: {e}")
    exit(1)

records = df.to_dict(orient='records')
print(f"Prepared {len(records)} records for insertion.")  # Debug print

db = client["PX_IDS"]
collection = db["phishing_data"]

try:
    if records:
        result = collection.insert_many(records)
        print(f"Inserted {len(result.inserted_ids)} records into MongoDB.")
    else:
        print("No records to insert.")
except Exception as e:
    print(f"Error inserting records: {e}")
