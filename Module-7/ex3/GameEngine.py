from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy

class GameEngine:
    def __init__(self):
        self.hand = []
        self.battlefield = []
        self.turn = 0
        self.damage_dealt = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict: 
        if len(self.battlefield) == 0:
            raise ValueError("Error, no enemy to simulate a turn")
        if len(self.hand) == 0:
            raise ValueError("Error, hand cannot be empty to simulate a turn")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        # try:
        print(f"Actions: {self.strategy.execute_turn(self.hand, self.battlefield)}")
        # except Exception as e:
            # print(e)

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turn,
            "strategy_used": self.strategy.strategy_name,
            "total_damage": self.damage_dealt,
            "cards_created": 1
            }