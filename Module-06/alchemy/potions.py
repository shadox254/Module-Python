from alchemy import create_fire, create_water
import alchemy.elements


def healing_potion():
    fire_result = create_fire()
    water_result = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion():
    earth_result = alchemy.elements.create_earth()
    fire_result = create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion():
    air_result = alchemy.elements.create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion():
    all_four_result = ""
    function_names = [
        "create_fire",
        "create_water",
        "create_earth",
        "create_air"
        ]
    i = 0
    for function in function_names:
        function_to_call = getattr(alchemy.elements, function)
        all_four_result += f"{function_to_call()}"
        i += 1
        if i < len(function_names):
            all_four_result += " and "
    return f"Wisdom potion brewed with all elements: {all_four_result}"
