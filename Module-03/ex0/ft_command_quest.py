import sys


def command_quest() -> None:
    """Displays and counts all given arguments."""
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        count = 1
        print(f"Program name: {sys.argv[0]}")
        arg_nb = len(sys.argv) - 1
        print(f"Arguments received: {arg_nb}")
        for i in range(arg_nb):
            print(f"Argument {count}: {sys.argv[count]}")
            count += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
