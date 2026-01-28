from random import randint
from typing import Any, Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal power
        power += power_to_add
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        try:
            return vault[key]
        except KeyError:
            return "Memory not found"
    return {
        "store": store,
        "recall": recall
        }


def main() -> None:
    print("Testing mage counter...")
    count = mage_counter()
    for i in range(0, 10):
        print(f"Call {i + 1}: {count()}")
    print()

    print("Testing spell accumulator...")
    initial_power = 0
    final_power = spell_accumulator(initial_power)
    print(f"Start power: {final_power(initial_power)}")
    for i in range(0, 3):
        power_to_add = randint(0, 100000000000000)
        print(f"Current power: {final_power(power_to_add)} \
({power_to_add} added)")
    print(f"Final power : {final_power(0)}")
    print()

    print("Testing enchantment factory...")
    enchantments = {
        "Impaling": "Trident",
        "Fire aspect": "Sword",
        "Punch": "Bow",
        "Quick Charge": "Crossbow",
        "Wind Burst": "Mace",
        "Curse of Vanishing": "Helmet",
        "Protection": "Chestplate",
        "Thorns": "Leggings",
        "Frost Walker": "Boots",
        "Luck of the Sea": "Fishing Rod",
        "Fortune": "Pickaxe"
    }
    for enchantment, item in enchantments.items():
        Merlin_the_Enchanter = enchantment_factory(enchantment)
        print(Merlin_the_Enchanter(item))
    print()

    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("power", 50)
    print("Recalling stored memory...")
    print(f"Power: {vault['recall']("power")}")
    print("Recalling no stored memory...")
    print(f"Power: {vault['recall']("powder")}")
    print()


if __name__ == "__main__":
    main()
