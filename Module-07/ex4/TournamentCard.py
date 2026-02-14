from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity, attack: int, health: int, id: str,
                 elo: int, wins: int, losses: int):
        if isinstance(id, str) is False:
            raise TypeError("Error, id must be an str")

        if isinstance(elo, int) is False:
            raise TypeError("Error, elo must be an int")
        if elo < 0:
            raise ValueError("Error, elo must be greater than 0")

        if isinstance(wins, int) is False:
            raise TypeError("Error, elo must be an int")
        if wins < 0:
            raise ValueError("Error, wins must be greater than 0")

        if isinstance(losses, int) is False:
            raise TypeError("Error, elo must be an int")
        if losses < 0:
            raise ValueError("Error, losses must be greater than 0")

        if isinstance(attack, int) is False:
            raise TypeError("Error, attack must be an int")
        if attack <= 0:
            raise ValueError("Error, attack must be greater or equal than 0")

        if isinstance(health, int) is False:
            raise TypeError("Error, health must be an int")
        if health <= 0:
            raise ValueError("Error, health must be greater or equal than 0")
        super().__init__(name, cost, rarity)
        self.attack_val = attack
        self.health_val = health
        self.id = id
        self.elo = elo
        self.wins = wins
        self.losses = losses
        self.defense = 0

    def play(self, game_state: dict) -> dict:
        if "incoming_damage" not in game_state:
            raise KeyError("Error, incoming_damage key does not exist")
        return (self.defend(game_state["incoming_damage"]))

    def attack(self, target) -> dict:
        if isinstance(target, Combatable) is False:
            raise TypeError("Error, target must be Combatable")
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_val,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        if isinstance(incoming_damage, int) is False:
            return TypeError("Error, damage must be an integer")
        if incoming_damage < 0:
            raise ValueError("Error, damage cannot be negative")

        damage_taken = incoming_damage - self.defense
        damage_blocked = self.defense
        if damage_taken <= 0:
            damage_taken = 0
            damage_blocked = incoming_damage
        self.health_val -= damage_taken

        if self.health_val <= 0:
            alive = False
        else:
            alive = True

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": alive
        }

    def get_combat_stats(self) -> dict:
        return ({
            "Attack": self.attack_val,
            "Defense": self.defense
        })

    def calculate_rating(self) -> int:
        try:
            new_elo = self.elo + int((self.wins + self.losses) / 2 * 8 +
                                     self.wins - self.losses)
        except ZeroDivisionError:
            raise ZeroDivisionError("Elo rating cannot change if no games are \
played")
        self.elo = new_elo
        return self.elo

    def update_wins(self, wins: int) -> None:
        if isinstance(wins, int) is False:
            raise ValueError("Error, wins must be an integer")
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        if isinstance(losses, int) is False:
            raise ValueError("Error, losses must be an integer")
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {"Rating": self.elo}
