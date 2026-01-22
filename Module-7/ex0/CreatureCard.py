from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.type = "Creature"
        try:
            int(attack)
        except ValueError:
            raise ValueError("Error, attack must be an integer")

        if attack < 0:
            raise ValueError("Error, attack must be greater than 0")
        self.attack = attack
        try:
            int(health)
        except ValueError:
            raise ValueError("Error, health must be an integer")

        if health < 0:
            raise ValueError("Error, health must be greater than 0")
        self.health = health

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
                "effect": "Creature summoned to battlefield"
            }
        return {
            "card_played": self.name,
            "effect": "Insufficient mana to summon the creature"
        }

    def attack_target(self, target: Card = None) -> dict:
        if target is None:
            raise ValueError("Error, target cannot be missing")
        if not isinstance(target, Card):
            raise ValueError("Error, target is not a Card")
        target.health -= self.attack
        if target.health <= 0:
            return {
                "attacker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": True
            }
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": False
        }

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value,
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        }
