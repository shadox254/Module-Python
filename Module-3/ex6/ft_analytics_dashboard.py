def list_comprehension(players: dict) -> None:
    """Demonstrates list comprehensions for filtering and transforming player data.

    Prints lists of high scorers, doubled scores, and active players based on 
    specific conditions.

    Args:
        players (list[dict]): A list of dictionaries, where each dictionary 
            represents a player's data.
    """
    print("=== List Comprehension Examples ===")
    high_scorers = [player['name'] for player in players if int(player['score']) > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    doubled_score = [player['score']*2 for player in players]
    print(f"Scores doubled: {doubled_score}")
    active_players = [player['name'] for player in players if player['status'] == 'active']
    print(f"Active players: {active_players}")


def dict_comprehension(players):
    """Demonstrates dictionary comprehensions for mapping and grouping data.

    Creates and prints dictionaries for player scores, score distribution categories 
    (high, medium, low), and achievement counts per player.

    Args:
        players (list[dict]): A list of dictionaries representing player data.
    """
    print("=== Dict Comprehension Examples ===")
    players_score = {player['name']: player['score'] for player in players}
    print(f"Player scores: {players_score}")
    score_categories = {
        'high': sum(1 for player in players if player['score'] > 2000),
        'medium': sum(1 for player in players if player['score'] > 1500 and player['score'] <= 2000),
        'low': sum(1 for player in players if player['score'] >= 0 and player['score'] <= 1500 )
    }
    print(f"Score categories: {score_categories}")
    achievement_count = {player['name']: len(player['achievement']) for player in players}
    print(f"Achievement counts: {achievement_count}")


def set_comprehension(players: dict) -> None:
    """Demonstrates set comprehensions for extracting unique values.

    Extracts and prints unique sets of player names, achievements, and regions
    to eliminate duplicates.

    Args:
        players (list[dict]): A list of dictionaries representing player data.
    """
    print("=== Set Comprehension Examples ===")
    unique_players = set(player['name'] for player in players)
    print(f"Unique players: {unique_players}")
    unique_achievement = set(achievement for player in players for achievement in player['achievement'])
    print(f"Unique achievements: {unique_achievement}")
    active_region = set(player['region'] for player in players)
    print(f"Active regions: {active_region}")


def combined_analysis(players: dict) -> None:
    """Performs aggregate analysis on the player dataset.

    Calculates and prints summary statistics including total player count, 
    total unique achievements, average score, and the top-performing player.

    Args:
        players (list[dict]): A list of dictionaries representing player data.
    """
    print("=== Combined Analysis ===")
    total_players = sum(1 for player in players)
    print(f"Total players: {total_players}")
    total_unique_achievement = sum(1 for achievement in set(achievement for player in players for achievement in player['achievement']))
    print(f"Total unique achievements: {total_unique_achievement}")
    average_score = sum(player['score'] for player in players) / (total_players)
    print(f"Average score: {average_score}")
    top_player = max((p['score'], p) for p in players)[1]
    print(f"Top performer: {top_player['name']} ({top_player['score']} points, {len(top_player['achievement'])} achievements)")


def analytics_dashboard(players: dict) -> None:
    """Orchestrates the execution of various comprehension examples.

    Acts as the main controller to run list, dictionary, set, and combined 
    analysis functions sequentially for the dashboard view.

    Args:
        players (list[dict]): A list of dictionaries representing player data.
    """
    print("=== Game Analytics Dashboard ===")
    print()
    list_comprehension(players)
    print()
    dict_comprehension(players)
    print()
    set_comprehension(players)
    print()
    combined_analysis(players)


if __name__ == "__main__":
    players = [
        {
            'name': 'alice',
            'score': 2300,
            'achievement': ['first_kill', 'level_10', 'boss_slayer', 'first_defeat', 'first_win'],
            'status': 'active',
            'region': 'north'
        },
        {
            'name': 'bob',
            'score': 1800,
            'achievement': ['first_kill', 'level_10', 'boss_slayer'],
            'status': 'active',
            'region': 'central'
        },
        {
            'name': 'charlie',
            'score': 2150,
            'achievement': ['first_kill', 'level_10', 'boss_slayer', 'first_defeat', 'first_win', 'Gg!', 'Top_#1!'],
            'status': 'active',
            'region': 'north'
        },
        {
            'name': 'diana',
            'score': 2050,
            'achievement': ['Top_#1!', 'first_death'],
            'status': 'inactive',
            'region': 'central'
        },
        {
            'name': 'Emmanuel'
            ,'score': 1500,
            'achievement': ['pokemon_trainer', 'complete_collection!', 'babyfoot?', 'Kratos?!'],
            'status': 'inactive',
            'region': 'east'
        },
        {
            'name': 'Amelie'
            ,'score': 1501,
            'achievement': ['dragonborn', 'One_ring_to_rule_them_all', 'League_of_Draven', 'GLaDOS?!'],
            'status': 'inactive',
            'region': 'west'
        }
    ]
    analytics_dashboard(players)
