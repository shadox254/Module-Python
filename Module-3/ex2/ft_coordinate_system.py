import sys
import math


def str_coordinates(first_coord: tuple):
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
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance


def coordinate_system():
    test1 = (10, 20, 5)
    str_coordinates(test1)
    print()

    test2 = ("3,4,0")
    str_coordinates(test2)
    print()

    test3 = ("abc,def,ghi")
    str_coordinates(test3)
    print()

    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            str_coordinates(sys.argv[1])
            print()
        elif len(sys.argv) == 4:
            args_tuple = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
            str_coordinates(args_tuple)
            print()
        else:
            print(f"Invalid number of arguments. Usage: python3 {sys.argv[0]} "
                  "<x> <y> <z> OR <\"x,y,z\">")
            print()

    print("Unpacking demonstration:")
    coord = test2.split(",")
    coord_tuple = tuple(int(number) for number in coord)
    x1, y1, z1 = coord_tuple
    print(f"Player at x={x1}, y={y1}, z={z1}")
    print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")


if __name__ == "__main__":
    coordinate_system()
