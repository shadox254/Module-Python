from ex4.TournamentCard import TournamentCard
from random import randint


class TournamentPlatform():
    def __init__(self):
        self.tournament_participant = []
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if isinstance(card, TournamentCard) is False:
            raise TypeError("Error, participant must be TournamentCard")
        self.tournament_participant.append(card)
        return f"{card.name} now registered"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if len(self.tournament_participant) < 2:
            raise ValueError("Error, not enough cards registered")

        if card1_id == card2_id:
            raise ValueError("Error, card1 and card2 are the same participant")

        card1 = None
        card2 = None
        for card in self.tournament_participant:
            if card1_id == card.id:
                card1 = card
            elif card2_id == card.id:
                card2 = card
            if card1 is not None and card2 is not None:
                break

        if card1 is None:
            raise ValueError(f"Error, {card1_id} is not a participant")
        if card2 is None:
            raise ValueError(f"Error, {card2_id} is not a participant")

        side_choice = randint(0, 1)
        if side_choice == 0:
            attacker = card1
            defender = card2
        else:
            attacker = card2
            defender = card1

        while attacker.health_val > 0 and defender.health_val > 0:
            attack_info = attacker.attack(defender)
            defender.defend(attack_info["damage"])

            if defender.health_val <= 0:
                break

            riposte_info = defender.attack(attacker)
            attacker.defend(riposte_info["damage"])

        if attacker.health_val <= 0:
            winner = defender
            loser = attacker
        else:
            winner = attacker
            loser = defender

        winner.update_wins(1)
        loser.update_losses(1)
        winner.calculate_rating()
        loser.calculate_rating()

        self.matches_played += 1

        return ({
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.elo,
            "loser_rating": loser.elo
        })

    def get_leaderboard(self) -> list:
        return sorted(self.tournament_participant, key=lambda p: p.elo,
                      reverse=True)

    def generate_tournament_report(self) -> dict:
        if len(self.tournament_participant) == 0:
            return {
                "total_cards": 0,
                "matches_played": 0,
                "avg_rating": 0,
                "platform_status": "inactive"
            }
        avg_rating = (sum(participant.elo
                      for participant in self.tournament_participant)
                      / len(self.tournament_participant))

        if self.matches_played == 0:
            platform_status = "inactive"
        else:
            platform_status = "active"
        return {
            "total_cards": len(self.tournament_participant),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": platform_status
        }
