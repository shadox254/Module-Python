from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: Rarity, attack: int,
                 defense: int, health: int, spell_name: str, spell_dmg: int,
                 spell_cost: int):
        try:
            int(attack)
        except ValueError:
            raise ValueError("Error, attack must be an integer")
        if attack < 0:
            raise ValueError("Error, attack must be greater than 0")

        try:
            int(defense)
        except ValueError:
            raise ValueError("Error, defense must be an integer")
        if defense < 0:
            raise ValueError("Error, defense must be greater than 0")

        try:
            int(health)
        except ValueError:
            raise ValueError("Error, health must be an integer")
        if health < 0:
            raise ValueError("Error, health must be greater than 0")

        try:
            if spell_name is None or spell_name == "":
                raise ValueError
        except ValueError:
            raise ValueError("Error, spell name cannot be empty")

        try:
            int(spell_dmg)
        except ValueError:
            raise ValueError("Error, spell_dmg must be an integer")
        if spell_dmg < 0:
            raise ValueError("Error, spell_dmg must be greater than 0")

        try:
            int(spell_cost)
        except ValueError:
            raise ValueError("Error, spell_cost must be an integer")
        if spell_cost < 0:
            raise ValueError("Error, spell_cost must be greater than 0")

        super().__init__(name, cost, rarity)
        self.attack_val = attack
        self.defense = defense
        self.health = health
        self.spell_name = spell_name
        self.spell_dmg = spell_dmg
        self.spell_cost = spell_cost
        self.type = "Elite"

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
                "effect": "Elite summoned to battlefield"
            }
        return {
            "card_played": self.name,
            "effect": "Insufficient mana to summon the creature"
        }

    def attack(self, target: Card) -> dict:
        if (isinstance(target, CreatureCard) is False
                and isinstance(target, EliteCard) is False):
            raise TypeError("Error, target must be a Creature or a Elite")
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
        if damage_taken > self.health:
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
        return {
            "attack": self.attack_val,
            "defense": self.defense,
            "health": self.health
        }

    def cast_spell(self, spell_name: str = None,
                   targets: list[Card] = None) -> dict:
        if spell_name is None:
            raise ValueError("No spell to cast")
        if targets is None:
            raise ValueError("Error, no target to cast the spell")
        dead_targets = 0
        targets_list = []
        for card in targets:
            card.health -= 3
            if card.health <= 0:
                dead_targets += 1
            targets_list.append(card.name)
        return {
            "caster": self.name,
            "spell": self.spell_name,
            "targets": targets_list,
            "dead_targets": dead_targets,
            "spell_damage": self.spell_dmg,
            "mana_used": self.spell_cost
        }

    def channel_mana(self, amount: int) -> dict:
        if amount <= 0:
            raise ValueError("Error, amount must be greater than 0")
        return {
            "channeled": amount,
            "total_mana": 7
        }

    def get_magic_stats(self) -> dict:
        return {
            "spell_name": self.spell_name,
            "spell_damage": self.spell_dmg,
            "spell cost": self.spell_cost,
            "total_mana": 7
        }
