def water_plants(plant_list):
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")

            
def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    print("Opening watering system")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Watering completed successfully!")
    print()
    print("Testing with error...")
    print("Opening watering system")
    plant_list = ["tomato", None]
    water_plants(plant_list)
    print()
    print("Cleanup always happens, even with errors!")


if (__name__ == "__main__"):
    test_watering_system()