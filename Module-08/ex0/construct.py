import sys
import os
from site import getsitepackages


def not_in_env() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()

    # sys.executable returns the path to the executable.
    # sys.version_info_minor returns the minor version number.
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
    print("activate     # On Windows")
    print()

    print("Then run this program again.")


def in_env() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print()

    # sys.executable returns the path to the executable.
    # os.path.basename(sys.prefix) Return the name of the folder where the
    #       Python environment is installed.
    # sys.prefix returns the path of python on the env
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print()

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print()

    print("Package installation path:")
    # sys.path_importer_cache() returns a list of strings containing
    #       the absolute paths to the site-packages directories
    print(getsitepackages()[0])


if __name__ == "__main__":
    # sys.prefix returns the path of python on the env
    # sys.base_prefix returns the path to the base Python installation,
    #       cannot be changed on env
    if sys.prefix == sys.base_prefix:
        not_in_env()
    else:
        in_env()
