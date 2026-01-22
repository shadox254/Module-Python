from ex3.FantasyCardFactory import FantasyCardFactory
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex3.AggressiveStrategy import AgressiveStrategy
from ex3.GameEngine import GameEngine
import random

def main():
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AgressiveStrategy()
    game = GameEngine()
    print(f"Factory: {factory.factory_name}")
    print(f"Strategy: {strategy.strategy_name}")
    print("Available types: \n{")
    for key, value in factory.types.items():
        print(f"'{key}': {value},")
    print("}")
    print()

    print("Simulating aggressive turn...")
    all_cards = (list(factory.creatures.values()) +
                 list(factory.spells.values()) +
                 list(factory.artifacts.values()))
    selection = random.sample(all_cards, 5)
    hand = []
    for card in selection:
        formatted_result = [f"{card['name']} ({card['cost']})"]
        game.hand.append(card)
        hand.append(card)
    print(formatted_result)
    print()

    game.configure_engine(factory, strategy)

    print("Turn execution:")
    Enemy1 = CreatureCard("Enemy1", 1, Rarity.COMMON, 1, 20)
    Enemy2 = CreatureCard("Enemy2", 1, Rarity.COMMON, 1, 1)
    game.battlefield.append(Enemy1)
    game.battlefield.append(Enemy2)
    game.simulate_turn()


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===\n")
    main()
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")

# if __name__ == "__main__":
#     factory = FantasyCardFactory()

#     print("--- Test Création Unitaire ---")
#     creature = factory.create_creature("Dragon")
#     print(creature.name)

#     spell = factory.create_spell("Fireball")
#     print(spell.name)

#     artifact = factory.create_artifact("Mana ring")
#     print(artifact.name)

#     print("\n--- Test Deck ---")
#     deck = factory.create_themed_deck(5)
#     print(f"Taille du deck : {deck['deck_size']}")
#     for category in ["creatures", "spells", "artifacts"]:
#         cards_list = deck[category]
#         if cards_list:
#             print(f"\n[{category.capitalize()}]")
#             for card_data in cards_list:
#                 print(f"  - {card_data['name']} (Coût: {card_data['cost']})")

#     print("-------------------------------------------------------------------------------------------------------"
#     "-------------------------------------------------------------------------------------------------------"
#     "-------------------------------------------------------------------------------------------------------"
#     "-------------------------------------------------------------------------------------------------------"
#     "-------------------------------------------------------------------------------------------------------"
#     "-------------------------------------------------------------------------------------------------------")

#     strategy = AgressiveStrategy()
#     goblin = CreatureCard("Goblin", 2, Rarity.COMMON, 4, 2)
#     dragon = CreatureCard("Dragon", 5, Rarity.LEGENDARY, 50, 5)
#     hand = [dragon, goblin]
#     rat = CreatureCard("Rat", 1, Rarity.COMMON, 1, 2)
#     giant = CreatureCard("Giant", 6, Rarity.EPIC, 4, 10)
#     battlefield = [giant, rat]

#     print(f"Stratégie active : {strategy.get_strategy_name()}")
#     print(f"Actions: {strategy.execute_turn(hand, battlefield)}")