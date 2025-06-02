from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import os

uri = os.getenv("MONGODB_URI")

client = MongoClient(uri, server_api=ServerApi('1'))


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    exit(1)


csv_path = os.path.join(os.path.dirname(__file__), "Phishing_Legitimate_full.csv")

try:
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} records from CSV.")
except Exception as e:
    print(f"Error reading CSV file: {e}")
    exit(1)


records = df.to_dict(orient='records')


db = client["PX_IDS"]
collection = db["phishing_data"]


try:
    result = collection.insert_many(records)
    print(f"Inserted {len(result.inserted_ids)} records into MongoDB.")
except Exception as e:
    print(f"Error inserting records: {e}")
