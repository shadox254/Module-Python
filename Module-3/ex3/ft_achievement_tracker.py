def print_achievement(players):
    for player in players:
        print(f"Player {player} achievements: {{", end="")
        for achievement in player.achievement:
            print(f"{achievement}")


def achievement_tracker():
    print("=== Achievement Tracker System ===")
    alice = {'achievement': ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon']}
    bob = {'achievement': ['first_kill', 'level_10', 'boss_slayer', 'collector']}
    charlie = {'achievement': ['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist']}
    players = [alice, bob, charlie]
    print_achievement(players)


if __name__ == "__main__":
    achievement_tracker()