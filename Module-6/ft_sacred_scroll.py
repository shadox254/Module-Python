import alchemy


def sacred_scroll():
    print("=== Sacred Scroll Mastery ===")
    print()

    print("Testing direct module access:")
    fire = f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}"
    water = f"alchemy.elements.create_water(): {alchemy.elements.create_water()}"
    earth = f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}"
    air = f"alchemy.elements.create_air(): {alchemy.elements.create_air()}"
    elements = [fire, water, earth, air]
    print(*elements, sep="\n")
    print()

    print("Testing package-level access (controlled by __init__.py):")
    functions = ["create_fire", "create_water", "create_earth", "create_air"]
    for function in functions:
        try:
            spell = getattr(alchemy, function)
            print(f"alchemy.{function}(): {spell()}")
        except AttributeError:
            print(f"alchemy.{function}(): AttributeError - not exposed")
    print()

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__=="__main__":
    sacred_scroll()
