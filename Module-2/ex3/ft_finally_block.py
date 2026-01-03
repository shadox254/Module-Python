def water_plants(plant_list: list[str]) -> None:
    """Waters each plant in the provided list.

    Args:
        plant_list (list[str]): List of plant names to water.

    Raises:
        ValueError: If a plant in the list is None.
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
        Runs test cases to simulate the watering system behavior under normal
        and error conditions.
    """
    print("=== Garden Watering System ===")
    print()
    print("Testing normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Watering completed successfully!")
    print()
    print("Testing with error...")
    plant_list = ["tomato", None]
    water_plants(plant_list)
    print()
    print("Cleanup always happens, even with errors!")


if (__name__ == "__main__"):
    test_watering_system()
