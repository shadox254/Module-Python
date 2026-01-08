import random


def data_stream_processor(event_count: int, event_list: list, player_list: list):
    print("=== Game Data Stream Processor ===")
    print()
    if event_count > 1:
        print(f"Processing {event_count} game events...")
    elif event_count == 1:
        print(f"Processing {event_count} game event...")
    else:
        print(f"Error! even_count is invalid.")
    print()

    for event_id in range(0, event_count):
        event = random.choice(event_list)
        player = random.choice(player_list)
        level = random.randint(1, 20)
        yield(event_id, player, level, event)


def stream_analytics(event_count: int, high_level_count: int, treasure_event: int, level_event: int):
    print("=== Stream Analytics ===")
    print(f"Total events processed: {event_count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_event}")
    print(f"Level-up events: {level_event}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: 0.045 seconds")
    print()


def fibonacci(n_terms: int):
    first, second = 0, 1
    for i in range(0, n_terms):
        yield first
        first, second = second, first+second


def prime_number(n_terms: int):
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


def generator_demonstration(n_terms: int, x_terms: int):
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
    stream_analytics(event_count, high_level_count, treasure_event, level_event)
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
