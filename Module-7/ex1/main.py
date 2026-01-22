#!/usr/bin/env python3
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.SpellCard import SpellCard, Effect
from ex1.ArtifactCard import ArtifactCard, Ability
from ex1.Deck import Deck
import sys


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print()

    print("Building deck with different card types...")
    deck = Deck()
    try:
        lightning_bolt = SpellCard("Lightning Bolt", 3, Rarity.COMMON,
                                   Effect.DMG)
    except ValueError as e:
        print(e)
        sys.exit(2)

    try:
        mana_crystal = ArtifactCard("Mana Crystal", 2, Rarity.UNCOMMON, 1,
                                    Ability.MANA)
    except ValueError as e:
        print(e)
        sys.exit(2)

    try:
        fire_dragon = CreatureCard("Fire Dragon", 7, Rarity.LEGENDARY, 6, 7)
    except ValueError as e:
        print(e)
        sys.exit(2)

    try:
        blob = CreatureCard("Blob", 6, Rarity.SECRET, 100, 100)
    except ValueError as e:
        print(e)
        sys.exit(2)

    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)

    print(f"Deck stats: {deck.get_deck_stats()}")
    print()

    print("Drawing and playing cards:")
    print()
    game_state = {
        "mana_available": 1000,
        "targets": blob,
        "deck": deck
    }
    for card in deck.deck:
        print(f"Drew: {card.name} ({card.type})")
        try:
            print(f"Play result: {card.play(game_state)}")
        except (TypeError, KeyError, ValueError) as e:
            print(e)
            sys.exit(2)
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
