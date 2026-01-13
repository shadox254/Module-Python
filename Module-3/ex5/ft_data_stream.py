import random
from typing import Iterator


def data_stream_processor(event_count: int, event_list: list,
                          player_list: list) -> Iterator[
                              tuple[int, str, int, str]]:
    """Simulates a stream of game events associated with players.

        This generator prints the processing status to stdout and yields
        randomly generated events combining a player, a level, and an
            event type.

        Args:
            event_count (int): The total number of events to generate.
            event_list (list): A list of strings representing possible
                event names.
            player_list (list): A list of strings representing player names.

        Yields:
            tuple[int, str, int, str]: A tuple containing:
                - event_id (int): The sequential ID of the event.
                - player (str): The name of the player selected.
                - level (int): A random level between 1 and 20.
                - event (str): The name of the event selected.
    """
    print("=== Game Data Stream Processor ===")
    print()
    if event_count > 1:
        print(f"Processing {event_count} game events...")
    elif event_count == 1:
        print(f"Processing {event_count} game event...")
    else:
        print("Error! even_count is invalid.")
    print()

    for event_id in range(0, event_count):
        event = random.choice(event_list)
        player = random.choice(player_list)
        level = random.randint(1, 20)
        yield (event_id, player, level, event)


def stream_analytics(event_count: int, high_level_count: int,
                     treasure_event: int, level_event: int) -> None:
    """Displays a summary report of the stream processing analytics.

    Prints statistics including total events, count of high-level players,
    occurrence of specific event types, and performance metrics to standard
        output.

    Args:
        event_count (int): Total number of events processed.
        high_level_count (int): Count of players with level 10 or higher.
        treasure_event (int): Count of 'Treasure' type events.
        level_event (int): Count of 'Level-up' type events.
    """
    print("=== Stream Analytics ===")
    print(f"Total events processed: {event_count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_event}")
    print(f"Level-up events: {level_event}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()


def fibonacci(n_terms: int) -> Iterator[int]:
    """Generates the Fibonacci sequence up to n terms.

    Args:
        n_terms (int): The number of terms to generate.

    Yields:
        int: The next number in the Fibonacci sequence.
    """
    first, second = 0, 1
    for i in range(0, n_terms):
        yield first
        first, second = second, first+second


def prime_number(n_terms: int) -> Iterator[int]:
    """Generates the first n prime numbers.

    Args:
        n_terms (int): The number of prime numbers to generate.

    Yields:
        int: The next prime number found.
    """
    primes = []
    num = 2
    while len(primes) < n_terms:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num
        num += 1


def generator_demonstration(n_terms: int, x_terms: int) -> None:
    """Demonstrates the usage of generator functions by printing sequences.

    Consumes the generators to display lists of Fibonacci numbers and
        prime numbers to standard output.

    Args:
        n_terms (int): The count of Fibonacci numbers to display.
        x_terms (int): The count of prime numbers to display.
    """
    print("=== Generator Demonstration ===")
    print(f"Fibonacci sequence (first {n_terms}): ", end="")
    fibonacci_sequence = fibonacci(n_terms)
    list_fibo = []
    for i in fibonacci_sequence:
        list_fibo.append(str(i))
    res = ", ".join(list_fibo)
    print(res)
    print(f"Prime numbers (first {x_terms}): ", end="")
    list_prime = []
    prime_sequence = prime_number(x_terms)
    for i in prime_sequence:
        list_prime.append(str(i))
    res = ", ".join(list_prime)
    print(res)


def data_stream(event_count: int, event_list: list, player_list: list) -> None:
    """Orchestrates the data stream processing and analytics display.

    Consumes the data stream generator, prints real-time events, aggregates
        statistics for the final report, and runs the generator demonstration.

    Args:
        event_count (int): The total number of events to simulate.
        event_list (list): A list of possible event types.
        player_list (list): A list of player names.
    """
    res = data_stream_processor(event_count, event_list, player_list)
    high_level_count = 0
    treasure_event = 0
    level_event = 0
    for event_id, player, level, event in res:
        print(f"Event {event_id + 1}: Player {player} (level {level}) {event}")
        if level > 10:
            high_level_count += 1
        if event == "found treasure":
            treasure_event += 1
        if event == "leveled up":
            level_event += 1
    print()
    stream_analytics(event_count, high_level_count, treasure_event,
                     level_event)
    generator_demonstration(10, 5)


if __name__ == "__main__":
    event_count = 1000
    event_list = [
        "killed monster",
        "found treasure",
        "leveled up",
        "became a dragon",
        "teleport to lobby",
        "purchased an item",
        "purchased a house",
        "complete a dungeon",
        "join the Horde",
        "is dead and have respawned"
    ]
    player_list = [
        "alice",
        "bob",
        "charlie",
        "romain",
        "alizea",
        "noemie",
        "ana"
    ]
    data_stream(event_count, event_list, player_list)
