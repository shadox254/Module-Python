import sys
import os

def not_in_env():
    print("MATRIX STATUS: You're still plugged in")
    print()

    print(f"Current python: {sys.executable}.{sys.version_info.minor}")
    print("Virtual Environment: None detected")
    print()

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows")
    print()

    print("Then run this program again.")


def in_env():
    print("MATRIX STATUS: Welcome to the construct")
    print()

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print()

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print()

    print("Package installation path:")
    print(sys.path_importer_cache)


if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        not_in_env()
    else:
        in_env()