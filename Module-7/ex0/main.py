#!/usr/bin/env python3
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
import sys


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print()

    print("Testing Abstract Base Class Design:")
    print()
    try:
        fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
        goblin_warrior = CreatureCard("Goblin Warrior", 3, Rarity.COMMON, 3, 5)
    except ValueError as e:
        print(e)
        sys.exit(2)

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())
    print()

    mana_available = 6
    print(f"Playing {fire_dragon.name} with {mana_available} mana available:")
    try:
        print(f"Playable: {fire_dragon.is_playable(mana_available)}")
    except (ValueError, TypeError) as e:
        print(e)
        sys.exit(2)
    try:
        print(f"Play result: {fire_dragon.play({"mana_available": 10})}")
    except (ValueError, KeyError, TypeError) as e:
        print(e)
        sys.exit(2)
    print()

    print(f"{fire_dragon.name} attacks {goblin_warrior.name}:")
    try:
        print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")
    except ValueError as e:
        print(e)
        sys.exit(2)
    print()

    mana_available = 3
    print(f"Testing insufficient mana ({mana_available} available):")
    print(f"Playable: {fire_dragon.is_playable(mana_available)}")
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
