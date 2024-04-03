def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start= 1):
        print(f"{index}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    summon_capt = [element.title() + "!" for element in planeteer_calls]
    return summon_capt
        

def long_planeteer_calls(calls):
    for word in calls:
        if len(word) > 4:
            return True
    return False

# First try
# def find_the_cheese(ingredients):
#     for item in ingredients:
#         cheeses = ["cheddar", "gouda", "camembert"]
#         for cheese in cheeses:
#             if item == cheese:
#                 return item
#     return None

# Refactored
def find_the_cheese(ingredients):
    cheeses = ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheeses:
            return ingredient
    return None
