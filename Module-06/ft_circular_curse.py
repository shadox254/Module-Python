from alchemy.grimoire import record_spell, validate_ingredients


def circular_curse_test():
    print("=== Circular Curse Breaking ===")
    print()

    print("Testing ingredient validation:")
    to_validate = "fire air"
    print(f"{validate_ingredients.__name__}(\"{to_validate}\"): "
          f"{validate_ingredients(to_validate)}")
    to_validate = "dragon scales"
    print(f"{validate_ingredients.__name__}(\"{to_validate}\"): "
          f"{validate_ingredients(to_validate)}")
    print()

    print("Testing spell recording with validation:")
    spell_name = "Fireball"
    ingredients = "fire air"
    print(f"{record_spell.__name__}({spell_name}, {ingredients}): "
          f"{record_spell(spell_name, ingredients)}")
    spell_name = "Dark Magic"
    ingredients = "shadow"
    print(f"{record_spell.__name__}({spell_name}, {ingredients}): "
          f"{record_spell(spell_name, ingredients)}")
    print()

    print("Testing late import technique:")
    spell_name = "Lightning"
    ingredients = "air"
    print(f"{record_spell.__name__}({spell_name}, {ingredients}): "
          f"{record_spell(spell_name, ingredients)}")
    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    circular_curse_test()
