class GardenError(Exception):
    """Base class for all exceptions related to the garden module."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """
        Exception raised for errors specifically involving plant health
        or growth.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Exception raised when an irrigation or water level issue occurs."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


def get_water(water_level: int) -> None:
    """Checks if the current water level is sufficient.

        Args:
           water_level (int): The current amount of water in the tank.

        Raises:
            WaterError: If the water level is 20 or below.
    """
    if water_level <= 20:
        raise WaterError("Not enough water in the tank!")
    return None


def plant_status(plant_wilt: bool) -> None:
    """Evaluates the wilting status of a plant.

        Args:
            plant_wilt (bool): A boolean indicating if the plant is wilting.

        Raises:
            PlantError: If the plant_wilt flag is True.
    """
    if plant_wilt:
        raise PlantError("The tomato plant is wilting!")
    return None


def check_errors() -> None:
    """Demonstrates the usage and catching of custom garden exceptions."""
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


if __name__ == "__main__":
    check_errors()
