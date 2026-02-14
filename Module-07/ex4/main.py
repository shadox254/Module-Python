from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex4.Rankable import Rankable
import sys


def main():
    print("Registering Tournament Cards...")
    print()

    tournament = TournamentPlatform()

    try:
        fire_dragon = TournamentCard("Fire Dragon", 5, Rarity.LEGENDARY, 5, 10,
                                     "dragon_001", 1200, 0, 0)
        ice_wizard = TournamentCard("Ice Wizard", 3, Rarity.LEGENDARY, 3, 7,
                                    "wizard_001", 1150, 0, 0)
    except (ValueError, TypeError) as e:
        print(e)
        sys.exit(2)

    participants = [fire_dragon, ice_wizard]
    for participant in participants:
        try:
            print(tournament.register_card(participant))
            print(f"{participant.name} (ID: {participant.id}):")
            print(f"- Interfaces: [{Card.__name__}, {Combatable.__name__}, \
{Rankable.__name__}]")
            print(f"- Rating: {participant.elo}")
            print(f"- Record: {participant.wins}-{participant.losses}")
        except TypeError as e:
            print(e)
            sys.exit(2)
        print()

    print("Creating tournament match...")
    try:
        print(f"Match result: {tournament.create_match(fire_dragon.id,
                                                       ice_wizard.id)}")
    except ValueError as e:
        print(e)
        sys.exit(2)
    print()

    leaderboard = tournament.get_leaderboard()
    print("Tournament Leaderboard:")
    i = 1
    for participant in leaderboard:
        print(f"{i}. {participant.name} - Rating: {participant.elo} \
({participant.wins}-{participant.losses})")
        i += 1
    print()

    print("Platform Report:")
    print(tournament.generate_tournament_report())
    print()


if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===\n")
    main()
    print("=== Tournament Platform Successfully Deployed! ===\n\
All abstract patterns working together harmoniously!")
