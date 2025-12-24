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
    def __init__(self):
        self.garden = {}

    def add_plant(self, plant):
        if plant['name'] in self.garden:
            print("The plant is already in the garden.")
            return
        if not plant['name']:
            raise ErrorAddingPlant("Error adding plant: Plant name cannot be empty!")
        self.garden[plant['name']] = plant
        print(f"Added {plant['name']} successfully")


    def watering_plant(self, plant_name):
        plant = self.garden[plant_name]
        plant['water_level'] += 3
        print(f"Watering {plant_name} - success")

    def plant_status(self, plant_name):
        plant = self.garden[plant_name]
        print(f"{plant['name']}: healthy (water: {plant['water_level']}, sun: {plant['health']})")


def garden_management():
    print("=== Garden Management System ===")
    print()
    tomato = {
        "name": "tomato",
        "water_level": 5, 
        "health": 8
    }
    lettuce = {
        "name": "lettuce",
        "water_level": 8, 
        "health": 5
    }
    test = {
        "name": "",
        "water_level": 8, 
        "health": 2
    }
    plant_list = [tomato, lettuce, test]
    manager = GardenManager()
    print("Adding plants to garden...")
    for plant in plant_list:
        try:
            manager.add_plant(plant)
        except ErrorAddingPlant as e:
            print(f"{e}")

    print()
    plant_list = [tomato, lettuce]
    print("Watering plants...")
    print("Opening watering system")
    try:
        for plant in plant_list:
            manager.watering_plant(plant['name'])
    except WaterError as e:
            print(f"{e}")
    finally:
        print("Closing watering system (cleanup)")

    print()
    print("Checking plant health...")
    try:
        for plant in plant_list:
            manager.plant_status(plant['name'])
    except WaterError as e:
            print(f"{e}")
    for plant in plant_list:
        manager.plant_status(plant)

    print()
    print("Garden management system test complete!")


if __name__=="__main__":
    garden_management()