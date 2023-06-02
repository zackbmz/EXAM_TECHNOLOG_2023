def is_valid_burger(burger):
    price_valid = 10 <= burger.price <= 20
    allergens_valid = all(
        allergen not in ["crustacé", "poisson", "soja", "céleri", "mollusques"]
        for allergen in burger.allergens
    )
    cooking_valid = burger.cooking in ["saignant", "à point", "cuit"]
    scoville_units_valid = (
        5000 <= burger.scoville_units <= 6000 and burger.scoville_units % 1000 == 0
    )

    return price_valid and allergens_valid and cooking_valid and scoville_units_valid

def extract_allergens(burger):
    return burger["allergens"]
