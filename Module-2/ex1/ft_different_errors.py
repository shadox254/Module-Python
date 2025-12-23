def garden_operations(*, int_str=None, div=None, file=None,
                      plant=None) -> None:
    """
        Function that tests for errors, produces them,
        and does not prevent them.
    """
    if int_str is not None:
        int(int_str)

    if div is not None:
        10/div

    if file is not None:
        open(file)

    if plant is not None:
        key = {}
        key[plant]


def test_error_types() -> None:
    """
        Performs tests with garden_operations() that will cause errors.
        Returns a message for each error but does not stop the code
        from executing.
    """
    print("=== Garden Error Types Demo ===")
    print()

    print("Testing ValueError...")
    try:
        garden_operations(int_str="abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        print()

    print("Testing ZeroDivisionError...")
    try:
        garden_operations(div=0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        print()

    print("Testing FileNotFoundError...")
    try:
        file = "missing.txt"
        garden_operations(file=file)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{file}'")
        print()

    print("Testing KeyError...")
    try:
        plant = "plant"
        garden_operations(plant=plant)
    except KeyError:
        print(f"Caught KeyError: 'missing\\_{plant}'")
        print()

    print("Testing multiple errors together...")
    try:
        file = "missing.txt"
        plant = "plant"
        garden_operations(int_str="abc", div=0, file=file, plant=plant)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
        print()

    print("All error types tested successfully!")


if (__name__ == "__main__"):
    test_error_types()
