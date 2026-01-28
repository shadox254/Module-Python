import alchemy.elements
# from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water


def transmutation():
    print("=== Import Transmutation Mastery ===")
    print()

    print("Method 1 - Full module import:")
    print(f"{alchemy.elements.__name__}."
          f"{alchemy.elements.create_fire.__name__}(): "
          f"{alchemy.elements.create_fire()}")
    print()

    print("Method 2 - Specific function import:")
    print(f"{create_water.__name__}(): {create_water()}")
    print()

    print("Method 3 - Aliased import:")
    print(f"{heal.__name__}(): {heal()}")
    print()

    print("Method 4 - Multiple imports:")
    print(f"{alchemy.elements.create_earth.__name__}(): "
          f"{alchemy.elements.create_earth()}\n"
          f"{create_fire.__name__}(): {create_fire()}\n"
          f"")


if __name__ == "__main__":
    transmutation()
