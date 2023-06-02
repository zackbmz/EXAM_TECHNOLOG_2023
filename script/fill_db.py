##Ce fichier sert à remplir initialement notre bdd

from app import Burger
from pymongo import MongoClient

burgers_data = [
    {
        "prix": 15.99,
        "description": "Burger Deluxe",
        "allergenes": ["lactose", "gluten"],
        "cuisson": "à point",
        "scoville": 5000
    },
    {
        "prix": 12.49,
        "description": "Burger Végétarien",
        "allergenes": ["gluten"],
        "cuisson": "cuit",
        "scoville": 0
    },
    {
        "prix": 18.99,
        "description": "Burger Épicé",
        "allergenes": ["lactose", "gluten"],
        "cuisson": "saignant",
        "scoville": 6000
    }
]

client = MongoClient("mongodb://mongodb:27017")
db = client["burgerdb"]
burgers_collection = db["burgers"]

burgers_collection.insert_many(burgers_data)
