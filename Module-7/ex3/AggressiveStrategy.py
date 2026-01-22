from ex3.GameStrategy import GameStrategy

class AgressiveStrategy(GameStrategy):
    def __init__(self):
        self.strategy_name = "AggressiveStrategy"

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        card_played = []
        mana_used = 0
        targets_attacked = []
        damage_dealt = 0

        if not hand or not battlefield:
            return {
                "cards_played": [],
                "mana_used": 0,
                "targets_attacked": [],
                "damage_dealt": 0
            }

        sorted_hand = sorted(hand, key=lambda card: card.cost)
        prio_targets = self.prioritize_targets(battlefield)
        remaining_hand = sorted_hand[:]
        for target in prio_targets:
            for card in remaining_hand:
                if card.attack >= target.health:
                    card_played.append(card)
                    targets_attacked.append(target)
                    mana_used += card.cost
                    damage_dealt += card.attack
                    remaining_hand.remove(card)
                    break
        
        return {
            "cards_played": card_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }
    def get_strategy_name(self) -> str:
        return self.strategy_name

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, key=lambda enemy: enemy.health)

