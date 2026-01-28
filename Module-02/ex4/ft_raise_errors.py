def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Perform various tests using information about a plant.

    Args:
        plant_name (str): The name of the plant.
        water_level (int): The water level of the plant.
        sunlight_hours (int): The number of hours the plant should be
            exposed to sunlight.

    Returns:
        str: A success message if all tests are successful.

    Raises:
        ValueError: If plant_name is empty, water_level is out of range (1-10),
                        or sunlight_hours is out of range (2-12).
    """
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level <= 1:
        raise ValueError(f"Error: Water level {water_level} is too"
                         " low (max 11)")

    if water_level >= 10:
        raise ValueError(f"Error: Water level {water_level} is too"
                         " high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too"
                         " low (min 2)")

    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too"
                         " high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """
        Runs test cases to simulate the behavior of the plant verification
            system under normal conditions and in the event of an error.
    """
    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 5))
    except ValueError as e:
        print(e)
    print()
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(e)

    print()
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(e)

    print()
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e)

    print()
    print("All error raising tests completed!")


if (__name__ == "__main__"):
    test_plant_checks()
