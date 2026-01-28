from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from random import randint
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, 10, "fire"),
        "ice_enchant": partial(base_enchantment, 10, "ice"),
        "lightning_enchant": partial(base_enchantment, 10, "lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast_spell(arg: Any) -> str:
        return f"Unknow spell: {arg}"

    @cast_spell.register(int)
    def _(arg: int) -> str:
        return f"Spell dealt {arg} damage to the target"

    @cast_spell.register(str)
    def _(arg: str) -> str:
        return f"Enchant: {arg}"

    @cast_spell.register(list)
    def _(arg: list) -> str:
        return f"{len(arg)} spells can be used"

    return cast_spell


def main() -> None:
    print("Testing spell reducer...")
    spells = [
        randint(1, 40),
        randint(1, 40),
        randint(1, 40),
        randint(1, 40)
        ]
    print(f"spells: {spells}")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")
    print()

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"Enchantment:\n Power: {power}, Element: {element}, \
Target: {target}"
    print("Testing partial enchanter...")
    partial_enchant = partial_enchanter(base_enchantment)
    for enchant in partial_enchant:
        print(partial_enchant[enchant]("Sword"))
    print()

    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"dispatcher with an integer: {dispatcher(10)}")
    print(f"dispatcher with an string: {dispatcher("Fire aspect")}")
    print(f"dispatcher with an list: {dispatcher([1, 2, 3, 4])}")
    print(f"dispatcher with an unknow type: {dispatcher({"element": "Fire"})}")
    print()


if __name__ == "__main__":
    main()
