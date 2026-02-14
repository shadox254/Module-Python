from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "common"
    UNCOMMON = "uncomon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"
    MYTHIC = "mythic"
    ANCESTRAL = "ancestral"
    ALTERNATE = "alternate"
    SECRET = "secret"
    COLLECTOR = "collector"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if name is None:
            raise ValueError("Error, name cannot be empty")
        self.name = name

        try:
            int(cost)
        except ValueError:
            raise ValueError("Error, cost must be an integer")
        if cost < 1:
            raise ValueError("Error, cost must be greater than 0")
        self.cost = cost

        if isinstance(rarity, Rarity) is False:
            raise ValueError("Error, rarity must exist")
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        to_return = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value
        }
        return to_return

    def is_playable(self, available_mana: int = None) -> bool:
        if available_mana is None:
            raise TypeError("Error, available_mana must exist")
        try:
            int(available_mana)
        except ValueError:
            raise ValueError("Error, available_mana must be an integer")
        return (available_mana >= self.cost)
