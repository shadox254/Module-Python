from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard
import sys


def main() -> None:
    print("=== DataDeck Ability System ===")
    print()

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']\n"
          "- Combatable: ['attack', 'defend', 'get_combat_stats']\n"
          "- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()

    print("Combat phase:")
    try:
        arcane_warrior = EliteCard("Arcane Warrior", 5, Rarity.MYTHIC, 7, 3,
                                   10, "Arcane Momentum", 10, 7)
        Enemy = CreatureCard("Enemy", 1, Rarity.COMMON, 1, 20)
        Enemy1 = CreatureCard("Enemy1", 1, Rarity.COMMON, 1, 20)
        Enemy2 = CreatureCard("Enemy2", 1, Rarity.COMMON, 1, 1)
    except (ValueError, TypeError) as e:
        print(e)
        sys.exit(2)
    try:
        print(f"Attack result: {arcane_warrior.attack(Enemy)}")
    except TypeError as e:
        print(e)
        sys.exit(2)
    try:
        print(f"Defense result: {arcane_warrior.defend(5)}")
    except ValueError as e:
        print(e)
        sys.exit(2)
    print()

    print("Magic phase:")
    targets = [Enemy1, Enemy2]
    try:
        print(f"Spell cast: {arcane_warrior.cast_spell
                             (arcane_warrior.spell_name, targets)}")
    except ValueError as e:
        print(e)
        sys.exit(2)
    try:
        print(f"Mana channel: {arcane_warrior.channel_mana(3)}")
    except ValueError as e:
        print(e)
        sys.exit(2)
    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
