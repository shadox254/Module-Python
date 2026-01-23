from ex3.FantasyCardFactory import FantasyCardFactory
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine
import random


def main():
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
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
    game.hand = []

    for card_data in selection:
        name = card_data["name"]
        card_obj = None

        if name in factory.types["creatures"]:
            card_obj = factory.create_creature(name)
        elif name in factory.types["spells"]:
            card_obj = factory.create_spell(name)
        elif name in factory.types["artifacts"]:
            card_obj = factory.create_artifact(name)
        if card_obj:
            game.hand.append(card_obj)
            hand.append(f"{card_obj.name} ({card_obj.cost})")
    print(f"Hand: {hand}")
    print()

    game.configure_engine(factory, strategy)

    print("Turn execution:")
    Enemy1 = CreatureCard("Enemy1", 1, Rarity.COMMON, 1, 20)
    Enemy2 = CreatureCard("Enemy2", 1, Rarity.COMMON, 1, 1)
    game.battlefield.append(Enemy1)
    game.battlefield.append(Enemy2)

    turn_result = game.simulate_turn()
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {turn_result}")
    print()

    print("Game Report:")
    print(game.get_engine_status())


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===\n")
    main()
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility \
achieved!")
