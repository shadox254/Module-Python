import alchemy.transmutation
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life


def pathway_debate():
    print("=== Pathway Debate Mastery ===")
    print()

    print("Testing Absolute Imports (from basic.py):")
    print(f"{lead_to_gold.__name__}(): {lead_to_gold()}")
    print(f"{stone_to_gem.__name__}(): {stone_to_gem()}")
    print()

    print("Testing Relative Imports (from advanced.py):")
    print(f"{philosophers_stone.__name__}(): {philosophers_stone()}")
    print(f"{elixir_of_life.__name__}(): {elixir_of_life()}")
    print()

    print("Testing Package Access:")
    print(f"{alchemy.transmutation.lead_to_gold.__name__}(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print(f"{alchemy.transmutation.philosophers_stone.__name__}(): "
          f"{alchemy.transmutation.philosophers_stone()}")
    print()

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    pathway_debate()
