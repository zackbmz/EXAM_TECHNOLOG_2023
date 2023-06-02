def parse_burger_from_db(burger) -> dict:
    return {
        "_id": str(burger["_id"]),
        "price": burger["price"],
        "description": burger["description"],
        "allergens": burger["allergens"],
        "cooking": burger["cooking"],
        "scoville_units": burger["scoville_units"],
    }
