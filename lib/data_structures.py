spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy = [food["name"] for food in spicy_foods]
    return spicy

# get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    spicy = [food for food in spicy_foods if food["heat_level"] > 5]
    return spicy

# get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    spicy = [f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}" for food in spicy_foods]
    for item in spicy:
        print(item)

# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            print(food)
            return food

# get_spicy_food_by_cuisine(spicy_foods, 'American')

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    heat_levels = [food['heat_level'] for food in spicy_foods]

    if heat_levels:
        average = int(sum(heat_levels) / len(heat_levels))
        return average

# get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    if spicy_food:
        spicy_foods.append(spicy_food)
        return spicy_foods

print(create_spicy_food(spicy_foods, "pilau"))
