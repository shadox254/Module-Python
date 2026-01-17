import alchemy


def transmutation():
    print("=== Import Transmutation Mastery ===")
    print()

    print("Method 1 - Full module import:")
    spell = "create_fire"
    try:
        spell_func = getattr(alchemy, spell)
        print(f"alchemy.{spell}(): {spell_func()}",)
    except AttributeError:
        print(f"alchemy.{spell}(): AttributeError - not exposed")
    print()

    print("Method 2 - Specific function import:")
    spell = "create_water"
    try:
        spell_func = getattr(alchemy, spell)
        print(f"alchemy.{spell}(): {spell_func()}",)
    except AttributeError:
        print(f"alchemy.{spell}(): AttributeError - not exposed")


if __name__=="__main__":
    transmutation()