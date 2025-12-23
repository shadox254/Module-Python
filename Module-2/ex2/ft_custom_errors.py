class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


def check_errors():
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        raise PlantError("Caught PlantError: The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print()
    print("Testing WaterError...")
    try:
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("Testing catching all garden errors...")
    print()
    print("All custom error types work correctly!")



if (__name__=="__main__"):
    check_errors()
