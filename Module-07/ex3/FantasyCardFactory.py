from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard, Ability
from ex1.SpellCard import SpellCard, Effect
from ex3.CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.factory_name = "FantasyCardFactory"
        self.types = {
            "creatures": ["Dragon", "Goblin", "Mawile", "Lynel", "Exodia",
                          "Calcium, The greatest", "Tony Mcfuse",
                          "Archfiend Commander", "Theo", "Freddy Krueger",
                          "Nosferatu Zodd", "Toriel", "Evangelion Unit-01",
                          "Sukuna", "B-Rabbit", "Nintendo", "Phantom",
                          "Hollow Grimm", "Myself", "Davy Jones", "Skull Kid"],
            "spells": ["Fireball", "Emperor's Divide", "Moonlight Vigil",
                       "Tempered Fate", "Dragon's Rage", "Realm of Death"],
            "artifacts": ["Mana ring", "BFG 9000", "Keyblade", "F.L.U.D.D.",
                          "Tharkun", "Light saber"]
        }
        self.creatures = {
            "Dragon": {"name": "Dragon", "cost": 5, "rarity": Rarity.LEGENDARY,
                       "attack": 4, "health": 5},
            "Goblin": {"name": "Goblin", "cost": 2, "rarity": Rarity.COMMON,
                       "attack": 1, "health": 2},
            "Mawile": {"name": "Mawile", "cost": 3, "rarity": Rarity.RARE,
                       "attack": 3, "health": 2},
            "Lynel": {"name": "Lynel", "cost": 2, "rarity": Rarity.RARE,
                      "attack": 2, "health": 3},
            "Exodia": {"name": "Exodia", "cost": 10,
                       "rarity": Rarity.ANCESTRAL, "attack": 10, "health": 3},
            "Calcium, The greatest": {"name": "Calcium, The greatest",
                                      "cost": 2, "rarity": Rarity.SECRET,
                                      "attack": 4, "health": 2},
            "Tony Mcfuse": {"name": "Tony Mcfuse", "cost": 4,
                            "rarity": Rarity.EPIC, "attack": 3, "health": 3},
            "Archfiend Commander": {"name": "Archfiend Commander", "cost": 3,
                                    "rarity": Rarity.RARE,
                                    "attack": 2, "health": 2},
            "Freddy Krueger": {"name": "Freddy Krueger", "cost": 7,
                               "rarity": Rarity.LEGENDARY,
                               "attack": 9, "health": 5},
            "Nosferatu Zodd": {"name": "Nosferatu Zodd", "cost": 6,
                               "rarity": Rarity.MYTHIC,
                               "attack": 8, "health": 8},
            "Toriel": {"name": "Toriel", "cost": 1, "rarity": Rarity.COMMON,
                       "attack": 0, "health": 10},
            "Evangelion Unit-01": {"name": "Evangelion Unit-01", "cost": 6,
                                   "rarity": Rarity.SECRET,
                                   "attack": 10, "health": 5},
            "Sukuna": {"name": "Sukuna", "cost": 3, "rarity": Rarity.EPIC,
                       "attack": 5, "health": 2},
            "B-Rabbit": {"name": "B-Rabbit", "cost": 2,
                         "rarity": Rarity.UNCOMMON, "attack": 2, "health": 2},
            "Nintendo": {"name": "Nintendo", "cost": 100,
                         "rarity": Rarity.COMMON, "attack": 100, "health": 10},
            "Phantom": {"name": "Phantom", "cost": 4, "rarity": Rarity.EPIC,
                        "attack": 6, "health": 2},
            "Hollow Grimm": {"name": "Hollow Grimm", "cost": 5,
                             "rarity": Rarity.COLLECTOR,
                             "attack": 9, "health": 6},
            "Myself": {"name": "Myself", "cost": 10, "rarity": Rarity.COMMON,
                       "attack": 1, "health": 1},
            "Davy Jones": {"name": "Davy Jones", "cost": 3,
                           "rarity": Rarity.LEGENDARY,
                           "attack": 3, "health": 3},
            "Skull Kid": {"name": "Skull Kid", "cost": 4,
                          "rarity": Rarity.EPIC,
                          "attack": 3, "health": 4}
        }

        self.spells = {
            "Fireball": {"name": "Fireball", "cost": 2,
                         "rarity": Rarity.COMMON, "effect_type": Effect.DMG},
            "Emperor's Divide": {"name": "Emperor's Divide", "cost": 3,
                                 "rarity": Rarity.EPIC,
                                 "effect_type": Effect.DEBUFF},
            "Moonlight Vigil": {"name": "Moonlight Vigil", "cost": 1,
                                "rarity": Rarity.ANCESTRAL,
                                "effect_type": Effect.DMG},
            "Tempered Fate": {"name": "Tempered Fate", "cost": 3,
                              "rarity": Rarity.EPIC,
                              "effect_type": Effect.BUFF},
            "Dragon's Rage": {"name": "Dragon's Rage", "cost": 2,
                              "rarity": Rarity.RARE,
                              "effect_type": Effect.DMG},
            "Realm of Death": {"name": "Realm of Death", "cost": 1,
                               "rarity": Rarity.LEGENDARY,
                               "effect_type": Effect.DEBUFF}
        }

        self.artifacts = {
            "Mana ring": {"name": "Mana ring", "cost": 3,
                          "rarity": Rarity.COMMON, "durability": 5,
                          "effect": Ability.MANA},
            "BFG 9000": {"name": "BFG 9000", "cost": 4,
                         "rarity": Rarity.LEGENDARY, "durability": 1,
                         "effect": Ability.DMG},
            "Keyblade": {"name": "Keyblade", "cost": 4, "rarity": Rarity.EPIC,
                         "durability": 1, "effect": Ability.GUARD},
            "F.L.U.D.D.": {"name": "F.L.U.D.D.", "cost": 2,
                           "rarity": Rarity.RARE, "durability": 1,
                           "effect": Ability.MANA},
            "Tharkun": {"name": "Tharkun", "cost": 3,
                        "rarity": Rarity.LEGENDARY, "durability": 4,
                        "effect": Ability.DMG},
            "Light saber": {"name": "Light saber", "cost": 2,
                            "rarity": Rarity.MYTHIC, "durability": 5,
                            "effect": Ability.DMG}
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in self.types["creatures"]:
            creature = self.creatures[name_or_power]
            return CreatureCard(creature["name"],
                                creature["cost"],
                                creature["rarity"],
                                creature["attack"],
                                creature["health"])
        return CreatureCard(name_or_power, 1, Rarity.COMMON.value())

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in self.types["spells"]:
            spell = self.spells[name_or_power]
            return SpellCard(spell["name"],
                             spell["cost"],
                             spell["rarity"],
                             spell["effect_type"])
        return SpellCard(name_or_power, 1, Rarity.COMMON.value())

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in self.types["artifacts"]:
            artifact = self.artifacts[name_or_power]
            return ArtifactCard(artifact["name"],
                                artifact["cost"],
                                artifact["rarity"],
                                artifact["durability"],
                                artifact["effect"])
        return ArtifactCard(name_or_power, 1, Rarity.COMMON.value())

    def create_themed_deck(self, size: int) -> dict:
        try:
            size = int(size)
        except ValueError:
            raise ValueError("Error, size must be an integer")
        if size <= 0:
            raise ValueError("Error, size must be greater than 0")
        deck = {
            "deck_size": size,
            "creatures": [],
            "spells": [],
            "artifacts": []
        }
        if size == 1:
            deck["creatures"].append(random.choice(
                list(self.creatures.values())))
        elif size == 2:
            deck["creatures"].append(random.choice(
                list(self.creatures.values())))
            deck["spells"].append(random.choice(list(self.spells.values())))
        else:
            ratio_creature = [0.40, 0.50, 0.60]
            creature_nb = int(size * random.choice(ratio_creature))
            artifact_nb = random.randint(0, 2)
            spells_nb = int(size - creature_nb - artifact_nb)

            for i in range(creature_nb):
                deck["creatures"].append(random.choice(
                    list(self.creatures.values())))
            for i in range(artifact_nb):
                deck["artifacts"].append(random.choice(
                    list(self.artifacts.values())))
            for i in range(spells_nb):
                deck["spells"].append(random.choice(
                    list(self.spells.values())))
        return deck

    def get_supported_types(self) -> dict:
        return self.types
