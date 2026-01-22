from ex0.Card import Card
from enum import Enum


class Ability(Enum):
    MANA = "mana"
    DMG = "damage"
    GUARD = "guard"


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        if isinstance(durability, int) is False:
            raise ValueError("Error, durability must be an integer")
        if durability <= 0:
            raise ValueError("Error, durability must be greater than 0")
        if isinstance(effect, Ability) is False:
            raise ValueError("Error, effect must be exist")
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.ability = effect
        self.type = "Artifact"
        if effect == Ability.MANA:
            self.ability_effect = "Permanent: +1 mana per turn"
        elif effect == Ability.DMG:
            self.ability_effect = "Permanent: +1 damage per turn"
        elif effect == Ability.GUARD:
            self.ability_effect = "Permanent: -1 damage received per turn"

    def play(self, game_state: dict = None) -> dict:
        if game_state is None:
            raise TypeError("Error, game_state cannot be empty")
        if "mana_available" not in game_state:
            raise KeyError("Error, key: mana_available does not exist")
        try:
            int(game_state['mana_available'])
        except ValueError:
            raise ValueError("Error, mana_available value must be an integer")
        if self.is_playable(game_state["mana_available"]):
            return {
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": self.ability_effect
            }
        return {
            "card_played": self.name,
            "effect": "Insufficient mana to use the artifact"
        }

    def activate_ability(self) -> dict:
        if self.effect == Ability.MANA:
            print(f"{self.name} give you +1 mana this turn!")
        if self.effect == Ability.DMG:
            print(f"{self.name} give you +1 damage this turn!")
        if self.effect == Ability.GUARD:
            print(f"{self.name} give you +1 reduction damage this turn!")
        return {
            "effect": self.effect
        }
