import sys
import math


def display_distance_from_input(first_coord: tuple | str) -> None:
    """
        Check the value of first_coord.
        If it is a number, run the program as it should.
        Otherwise, display an error message without crashing the program.

        Arg:
            first_coord (tuple | str): corresponds to coordinates
                in the form of a tuple or character string.

        Return: Returns None if first_coord is invalid.

        Raise:
            ValueError: If in first_coord, there is something different
                from a number.
    """
    coord_tuple = ()
    if isinstance(first_coord, tuple):
        coord_tuple: tuple = first_coord
        print(f"Position created: {coord_tuple}")

    if isinstance(first_coord, str):
        coord = first_coord.split(",")
        try:
            coord_tuple = tuple(int(number) for number in coord)
            print(f"Parsing coordinates: \"{first_coord}\"")
            print(f"Parsed position: {coord_tuple}")
        except ValueError as e:
            print(f"Parsing invalid coordinates: \"{first_coord}\"\n"
                  f"Error parsing coordinates: {e}'\n"
                  f"Error details - Type: ValueError, Args: (\"{e}\",)")
            return None

    second_coord: tuple = (0, 0, 0)
    print(f"Distance between {second_coord} and {coord_tuple}: "
          f"{distance(coord_tuple):.2f}")

    # print()
    # print("Unpacking demonstration:")
    # x1, y1, z1 = coord_tuple
    # print(f"Player at x={x1}, y={y1}, z={z1}")
    # print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")


def distance(coord1: tuple, coord2: tuple = (0, 0, 0)) -> float:
    """
        Calculates the distance between the first coordinates and the
        second coordinates.

        Args:
            coord1 (tuple): tuple of int corresponding to the coordinates
                of the first point.
            coord2 (tuple): tuple of int corresponding to the coordinates
                of the second point, with the base tuple equal to (0, 0, 0).

        Return: Returns the distance between the two points as a float.
    """
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance


def coordinate_system() -> None:
    """
        Perform several tests with display_distance_from_input to see different
            behaviors of the function and if there are any crashes.
    """
    test1 = (10, 20, 5)
    display_distance_from_input(test1)
    print()

    test2 = ("3,4,5")
    display_distance_from_input(test2)
    print()

    test3 = ("abc,def,ghi")
    display_distance_from_input(test3)

    print()
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            display_distance_from_input(sys.argv[1])
        elif len(sys.argv) == 4:
            try:
                args_tuple = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
                display_distance_from_input(args_tuple)
            except ValueError as e:
                print(f"Parsing invalid coordinates: \"{sys.argv[1]},{sys.argv[2]},{sys.argv[3]}\"\n"
                      f"Error parsing coordinates: {e}'\n"
                      f"Error details - Type: ValueError, Args: (\"{e}\",)")
        else:
            print(f"Invalid number of arguments. Usage: python3 {sys.argv[0]} "
                  "<x> <y> <z> OR <\"x,y,z\">")

    print()
    print("Unpacking demonstration:")
    coord = test2.split(",")
    try:
        coord_tuple = tuple(int(number) for number in coord)
        x1, y1, z1 = coord_tuple
        print(f"Player at x={x1}, y={y1}, z={z1}")
        print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")
    except ValueError:
        print("Error: Unable to unpack, coordinates contain invalid characters.")


if __name__ == "__main__":
    coordinate_system()
