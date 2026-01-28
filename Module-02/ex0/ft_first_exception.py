def check_temperature(temp_str: str) -> int:
    """Check if the temp_str passed is valid or not.

        Args:
            temp_str (str): Temperature in str.

        Return: Return temp if it is valid, or None in other cases.
    """
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    else:
        if (temp < 0):
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        elif (temp > 40):
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp


def test_temperature_input() -> None:
    """Perform several tests for our check_temperature() function."""
    test = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===")
    for temp in test:
        print()
        check_temperature(temp)
    print()
    print("All tests completed - program didn't crash!")


if (__name__ == "__main__"):
    test_temperature_input()
