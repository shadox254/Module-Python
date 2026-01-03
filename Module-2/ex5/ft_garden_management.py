class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ErrorAddingPlant(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class GardenManager:
    def __init__(self, water_tank=10):
        """Initializes the garden manager with a water tank.

        Args:
            water_tank (int): Initial amount of water available.
            Defaults to 10.
        """
        self.garden = {}
        self.water_tank = water_tank

    def add_plant(self, plant: dict) -> None:
        """Adds a new plant to the garden dictionary.

        Args:
            plant (dict): Dictionary containing plant details.

        Raises:
            ErrorAddingPlant: If the plant name is empty or already exists.
        """
        if not plant.get('name'):
            raise ErrorAddingPlant("Error adding plant: Plant name cannot"
                                   " be empty!")
        if plant['name'] in self.garden:
            raise ErrorAddingPlant(f"Error adding plant: {plant['name']}"
                                   " is already in the garden!")
        self.garden[plant['name']] = plant
        print(f"Added {plant['name']} successfully")

    def watering_plant(self, plant_name: str) -> None:
        """Waters a specific plant and deducts water from the tank.

        Args:
            plant_name (str): The name of the plant to water.

        Raises:
            GardenError: If the plant is not found or if the water tank
            is insufficient.
        """
        if plant_name not in self.garden:
            raise GardenError(f"Plant {plant_name} not found in garden")
        water_needed = 5
        if self.water_tank < water_needed:
            raise GardenError("Not enough water in tank")
        if plant_name == "lettuce":
            self.garden[plant_name]['water_level'] += 7
        self.water_tank -= water_needed
        print(f"Watering {plant_name} - success")

    def plant_status(self, plant_name: str) -> None:
        """Displays the health status of a plant based on its water level.

        Args:
            plant_name (str): The name of the plant to check.

        Raises:
            WaterError: If the water level exceeds the safety threshold.
            KeyError: If the plant_name does not exist in the garden.
        """
        plant = self.garden[plant_name]
        if plant['water_level'] > 10:
            raise WaterError(f"Water level {plant['water_level']} is too"
                             " high (max 10)")
        print(f"{plant['name']}: healthy (water: {plant['water_level']},"
              " sun: {plant['sun']})")


def garden_management() -> None:
    """
    Simulates a garden management workflow to test system functionality.
    """
    print("=== Garden Management System ===")
    print()
    plants_list = [
        {"name": "tomato", "water_level": 5, "sun": 8},
        {"name": "lettuce", "water_level": 8, "sun": 5},
        {"name": "", "water_level": 8, "sun": 2}
    ]
    manager = GardenManager(10)

    print("Adding plants to garden...")
    for p in plants_list:
        try:
            manager.add_plant(p)
        except ErrorAddingPlant as e:
            print(e)

    print("\nWatering plants...")
    print("Opening watering system")
    try:
        for name in ["tomato", "lettuce"]:
            manager.watering_plant(name)
    except GardenError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    for name in ["tomato", "lettuce"]:
        try:
            manager.plant_status(name)
        except WaterError as e:
            print(f"Error checking {name}: {e}")

    print("\nTesting error recovery...")
    try:
        manager.watering_plant("lettuce")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    garden_management()
