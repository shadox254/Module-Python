from ex0.Card import Card
from random import shuffle


class Deck:
    def __init__(self):
        self.deck = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        try:
            self.deck.remove(card_name)
        except ValueError:
            return False
        return True

    def shuffle(self) -> None:
        shuffle(self.deck)

    def draw_card(self) -> Card:
        if len(self.deck) == 0:
            print("There are no more cards to draw.")
            return None
        card = self.deck.pop(0)
        return card

    def get_deck_stats(self) -> dict:
        total_cards = len(self.deck)
        if total_cards == 0:
            raise ValueError("Deck is empty")
        return {
            "total_card": total_cards,
            "creatures": sum(1 for card in self.deck if card.type ==
                             "Creature"),
            "spells": sum(1 for card in self.deck if card.type == "Spell"),
            "artifacts": sum(1 for card in self.deck if card.type ==
                             "Artifact"),
            "avg_cost": sum(card.cost for card in self.deck)/total_cards
        }
