def print_achievement(players: dict) -> None:
    """Displays all achievements for each player.

        Arg:
            players (dict): Dictionary containing all players in keys and
                their achievements in values.
    """
    print("=== Achievement Tracker System ===")
    print()
    for name, achievements in players.items():
        print(f"Player {name} achievements: {{", end="")
        i = 0
        for achievement in achievements:
            print(f"'{achievement}'", end="")
            i += 1
            if len(achievements) > i:
                print(", ", end="")
            else:
                print("}")
    print()


def achievement_analytics(players: dict):
    """Displays several analyses of player achievements.

        Arg:
            players (dict): Dictionary containing all players in keys and
                their achievements in values.
    """
    print("=== Achievement Analytics ===")
    unique_achievement = set()
    for achievements in players.values():
        for achievement in achievements:
            unique_achievement.add(achievement)
    # print("All unique achievements: {", end="")
    # sorted_unique_achievement = sorted(unique_achievement)
    # i = 0
    # for achievement in sorted_unique_achievement:
    #     print(f"'{achievement}'", end="")
    #     i += 1
    #     if len(sorted_unique_achievement) > i:
    #         print(", ", end="")
    #     else:
    #         print("}")
    print("All unique achievements: "
          f"{{{', '.join(f'{x!r}' for x in sorted(unique_achievement))}}}")
    print(f"Total unique achievements: {len(unique_achievement)}")
    print()


def achievements_rarity(players: dict) -> None:
    """Displays several messages regarding the rarity of achievements

        Arg:
            players (dict): Dictionary containing all players in keys and
                their achievements in values.
    """
    common_achievement = None
    for achievements in players.values():
        if not common_achievement:
            common_achievement = set(achievements)
        else:
            common_achievement = common_achievement.intersection(achievements)
    print("Common to all players: "
          f"{{{', '.join(f'{x!r}' for x in sorted(common_achievement))}}}")

    achievements_count = {}
    for achievements in players.values():
        for achievement in achievements:
            if achievement in achievements_count:
                achievements_count[achievement] += 1
            else:
                achievements_count[achievement] = 1

    rare_achievements = set()
    for achievement, i in achievements_count.items():
        if i == 1:
            rare_achievements.add(achievement)
    print("Rare achievements (1 player): "
          f"{{{', '.join(f'{x!r}' for x in sorted(rare_achievements))}}}")
    print()


def achievement_comp(p1_name: str, player_1_achv: list, p2_name: str,
                     player_2_achv: list) -> None:
    """
        Displays several comparisons between the achievements of
            player 1 and player 2.

        Args:
            p1_name (str): The name of player 1, which will be compared
                with player 2.
            player_1_achv (list): The list of all achievements for player 1.
            p2_name (str): The name of player 2, which will be compared
                with player 1.
            player_2_achv (list): The list of all achievements for player 2.
    """
    inter_p1_p2 = set.intersection(set(player_1_achv), set(player_2_achv))
    print(f"{p1_name.capitalize()} vs {p2_name.capitalize()} common: "
          f"{{{', '.join(f'{x!r}' for x in sorted(inter_p1_p2))}}}")

    only_p1 = set.difference(set(player_1_achv), set(player_2_achv))
    print(f"{p1_name.capitalize()} unique: "
          f"{{{', '.join(f'{x!r}' for x in sorted(only_p1))}}}")

    only_p2 = set.difference(set(player_2_achv), set(player_1_achv))
    print(f"{p2_name.capitalize()} unique: "
          f"{{{', '.join(f'{x!r}' for x in sorted(only_p2))}}}")


def achievement_tracker() -> None:
    """
        Create a dictionary of players and their achievements
            to be used in different functions.
    """
    players = {
        "alice": ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'],
        "bob": ['first_kill', 'level_10', 'boss_slayer', 'collector'],
        "charlie": ['level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist']
        }
    print_achievement(players)
    achievement_analytics(players)
    achievements_rarity(players)
    achievement_comp("alice", players["alice"], "bob", players["bob"])


if __name__ == "__main__":
    achievement_tracker()
