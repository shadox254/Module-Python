import sys


def score_analytics():
    print("=== Player Score Analytics ===")
    try:
        if (len(sys.argv) == 1):
            raise ValueError
    except ValueError:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} "
              "<score1> <score2> ...")
        return None
    try:
        for i in range(len(sys.argv) - 1):
            int(sys.argv[i + 1])
    except ValueError:
        print(f"One of the scores is invalid. Usage: python3 {sys.argv[0]} "
              "<score1> <score2> ...")
        return None

    score_list = []
    for arg in sys.argv[1:]:
        score_list.append(int(arg))
    print(f"Scores processed: {score_list}")
    print(f"Total players: {len(sys.argv) - 1}")
    res = sum(score_list)
    print(f"Total score: {res}")
    average_score = res/(len(sys.argv) - 1)
    print(f"Average score: {average_score}")
    max_score = max(score_list)
    print(f"High score: {max_score}")
    min_score = min(score_list)
    print(f"Low score: {min_score}")
    score_range = max_score - min_score
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    score_analytics()
