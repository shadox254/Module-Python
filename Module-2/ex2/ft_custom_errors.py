class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


def get_water(water_level: int):
    if (water_level <= 20):
        raise WaterError("Not enough water in the tank!")
    else:
        return


def plant_status(plant_wilt: bool):
    if (plant_wilt == True):
        raise PlantError("The tomato plant is wilting!")
    else:
        return


def check_errors():
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        plant_status(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        get_water(15)
    except WaterError as e:
        print(f"Caught a WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        plant_status(True)
    except GardenError as e:
        print(f"Caught a garden error: {e.args[0]}")
    try:
        get_water(20)
    except GardenError as e:
        print(f"Caught a garden error: {e.args[0]}")
    print()
    print("All custom error types work correctly!")



if (__name__=="__main__"):
    check_errors()
