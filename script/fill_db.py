from pymongo import MongoClient
from bson import ObjectId

MONGO_HOST = "mongodb"
DB_NAME = "burger_store"
BURGER_COLLECTION_NAME = "burgers"

client = MongoClient(MONGO_HOST)
db = client[DB_NAME]

burgers = [
    {
        "_id": ObjectId(),
        "prix": 12.5,
        "description": "Burger classique",
        "allergenes": ["lait", "gluten"],
        "cuisson": "à point",
        "scoville": 5000,
    },
    {
        "_id": ObjectId(),
        "prix": 15.0,
        "description": "Burger végétarien",
        "allergenes": ["gluten"],
        "cuisson": "saignant",
        "scoville": 6000,
    },
]

# Insérer les données
db[BURGER_COLLECTION_NAME].insert_many(burgers)
