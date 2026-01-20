from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from enum import Enum


class Effect(Enum):
    DMG = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        if effect_type is Effect.DMG:
            self.effect = "Deal 3 damage to target"
            self.effect_value = 3
        elif effect_type is Effect.HEAL:
            self.effect = "Heal 5 damage to target"
            self.effect_value = 5
        elif effect_type is Effect.BUFF:
            self.effect = "Buff attack target by 2"
            self.effect_value = 2
        elif effect_type is Effect.DEBUFF:
            self.effect = "Debuff attack target by 2"
            self.effect_value = 2
        else:
            raise ValueError(f"Error, {effect_type} is not valid")
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "Spell"

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
                "effect": self.effect
            }
        return {
            "card_played": self.name,
            "effect": "Insufficient mana to use the spell"
        }

    def resolve_effect(self, targets: list) -> dict:
        if len(targets) < 1:
            raise ValueError("Error, no target selected")
        for target in targets:
            if isinstance(target, CreatureCard) is False:
                raise TypeError(f"Error, {target} must be a creature")
            if self.effect_type is Effect.DMG:
                target.health -= self.effect_value
            elif self.effect_type is Effect.HEAL:
                target.health += self.effect_value
            elif self.effect_type is Effect.BUFF:
                target.attack += self.effect_value
            elif self.effect_type is Effect.DEBUFF:
                target.attack -= self.effect_value
            return targets
