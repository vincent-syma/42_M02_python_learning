#!/usr/bin/env python3

# ANSI
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

# combinations
BOLD_RED = BOLD + RED
BOLD_GREEN = BOLD + GREEN
BOLD_BLUE = BOLD + BLUE


def main() -> None:
    """
    Entry point of the analytics dashboard.
    """
    print()
    print(f"{BOLD_BLUE}=== Game Analytics Dashboard ==={RESET}")
    print()

    print(f"{BOLD}=== List Comprehension Examples ==={RESET}")
    print()
    scores = {'alice': 2300,
              'bob': 1800,
              'charlie': 2150,
              'diana': 2050}

    high_scorers = [player for player, score in scores.items() if score > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [score * 2 for score in scores.values()]
    print(f"Scores doubled: {scores_doubled}")
    print()

    print(f"{BOLD}=== Dict Comprehension Examples ==={RESET}")
    print()

    player_scores = {player: score for player, score in scores.items()
                     if score > 2000}
    print(f"Player scores: {player_scores}")

    score_categories = {
        'high': sum(1 for score in scores.values() if score > 2000),
        'medium': sum(1 for score in scores.values() if 1500 <= score <= 2000),
        'low': sum(1 for score in scores.values() if score < 1500)
    }
    print(f"Score categories: {score_categories}")

    achievements = {
        'alice': {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
        'bob': {'first_kill', 'level_10', 'boss_slayer', 'collector'},
        'charlie': {'level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist'}
    }
    ach_counts = {player: len(achievements_set) for player, achievements_set
                  in achievements.items()}
    print(f"Achievement counts: {ach_counts}")
    print()

    print(f"{BOLD}=== Set Comprehension Examples ==={RESET}")
    print()

    players_list = ['alice', 'bob', 'charlie', 'alice', 'diana', 'bob']
    players_set = sorted({player for player in players_list})
    print(f"Unique players: {players_set}")

    unique_ach = sorted({ach for ach_set in achievements.values()
                         for ach in ach_set})
    print(f"Unique achievements: {unique_ach}")
    print()

    print(f"{BOLD}=== Combined Analysis ==={RESET}")
    print()

    print(f"Total players: {len(players_set)}")
    print(f"Total unique achievements: {len(unique_ach)}")
    average_score = sum(scores.values()) / len(scores)
    print(f"Average score: {average_score:.1f}")
    top_player = max(scores, key=scores.get)
    top_score = scores[top_player]
    print(f"Top performer: {top_player} ({top_score} points)")
    print()


if __name__ == "__main__":
    main()
