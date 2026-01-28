from functools import wraps
from time import time
from typing import Any, Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        print(f"Casting {func.__name__}...")
        start = time()
        spell = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {(end - start):.3f} seconds")
        return spell

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            for arg in args:
                if isinstance(arg, int):
                    if arg >= min_power:
                        return func(*args, **kwargs)
                    else:
                        return "Not enough power to use this spell"
            return "Not enough power to use this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, {attempt} attempts out of \
{max_attempts} remain")
                attempt += 1
            return f"Spell failed after {max_attempts} retry"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3 and name.replace(" ", "").isalpha())

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        return "Fireball cast!"
    print(f"Result: {fireball()}")
    print()

    # print("Testing power validator...")
    # @power_validator(10)
    # def spell(power: int):
    #     return f"Spell cast with a power of {power}"
    # print(spell(21))
    # print()

    # print("Testing retry spell...")
    # feur_list = []
    # @retry_spell(50)
    # def quoi(boolean: bool) -> bool:
    #     if not boolean:
    #         feur_list.append("FEUR!")
    #         12/0
    #         return False
    #     return True
    # print(quoi(False))
    # if len(feur_list) > 0:
    #     for feur in feur_list:
    #         print(feur)
    # print()

    print("Testing MageGuild...")
    mageguild = MageGuild()
    print(MageGuild.validate_mage_name("Schierke"))
    print(MageGuild.validate_mage_name("Vel'Koz"))

    print(mageguild.cast_spell("Lightning", 15))
    print(mageguild.cast_spell("wrong spell", 1))


if __name__ == "__main__":
    main()
