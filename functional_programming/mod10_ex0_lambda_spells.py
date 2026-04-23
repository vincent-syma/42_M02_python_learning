#!/usr/bin/env python3

# ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

# combinations
BOLD_RED = BOLD + RED
BOLD_GREEN = BOLD + GREEN
BOLD_BLUE = BOLD + BLUE

# Authorized: map, filter, sorted, print()


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts by power (descending)"""
    return (sorted(artifacts, key=lambda a: a['power'], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages by power"""
    return (filter(lambda a: a['power'] > min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names"""
    return list((map(lambda a: f"* {a} *", spells)))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate mage statistics"""

    total_power = sum(map(lambda m: m['power'], mages))
    # sum(mage['power'] for mage in mages)

    return {
        'max_power': max(mages, key=lambda a: a['power'])['power'],
        # max(mage['power'] for mage in mages),

        'min_power': min(mages, key=lambda a: a['power'])['power'],
        # min(mage['power'] for mage in mages),

        'avg_power': round(total_power / len(mages), 2)
    }


# --- test functions ---

def test_sorter(artifacts: list[dict]) -> None:
    print(f"\n{ITALIC}Testing artifact sorter...{RESET}")

    print(f"\n{BOLD}Artifacts:{RESET}")
    print(", ".join(f"{a['name']} ({a['power']})" for a in artifacts))

    sorted_artifacts = artifact_sorter(artifacts)

    print(f"\n{BOLD}Sorted (descending):{RESET}")
    print(", ".join(f"{a['name']} ({a['power']})" for a in sorted_artifacts))

    # print(f"\n{BOLD}Artifacts:{RESET}",)
    # for artifact in artifacts:
    #     print(f"- {artifact['name']} ({artifact['power']} power)")

    # sorted = artifact_sorter(artifacts)

    # print(f"\n{BOLD}Sorted (descending):{RESET}",)
    # for artifact in sorted:
    #     print(f"- {artifact['name']} ({artifact['power']} power)")


def test_filter(mages: list[dict], min_power: int) -> None:
    print(f"\n{ITALIC}Testing power filter...{RESET}")

    print(f"\n{BOLD}Mages:{RESET}")
    print(", ".join(f"{m['name']} ({m['power']} power)" for m in mages))

    filtered = power_filter(mages, min_power)

    print(f"\n{BOLD}Filtered (more than {min_power} power):{RESET}")
    print(", ".join(f"{m['name']} ({m['power']} power)" for m in filtered))

    # print(f"\n{BOLD}Mages:{RESET}",)
    # for mage in mages:
    #     print(f"- {mage['name']} ({mage['power']} power)")

    # filtered = power_filter(mages, min_power)

    # print(f"\n{BOLD}Filtered (more than {min_power} power):{RESET}",)
    # for mage in filtered:
    #     print(f"- {mage['name']} ({mage['power']} power)")


def test_transformer(spells: list[str]) -> None:
    print(f"\n{ITALIC}Testing spell transformer...{RESET}")

    print(f"\n{BOLD}Spells:{RESET}")
    print(", ".join(spells))

    transformed = spell_transformer(spells)

    print(f"\n{BOLD}Transformed:{RESET}")
    print(", ".join(transformed))

    # print(f"\n{BOLD}Spells:{RESET}",)
    # for spell in spells:
    #     print(f"- {spell}")

    # transformed = spell_transformer(spells)

    # print(f"\n{BOLD}Transformed:{RESET}",)
    # for spell in transformed:
    #     print(f"- {spell}")


def test_stats(mages: list[dict]) -> None:
    print(f"\n{ITALIC}Testing mage stats...{RESET}")

    print(f"\n{BOLD}Mages:{RESET}")
    print(", ".join(f"{m['name']} ({m['power']})" for m in mages))

    stats = mage_stats(mages)

    print(f"\n{BOLD}Mage stats:{RESET}")
    print(", ".join(f"{key}: {value}" for key, value in stats.items()))

    # print(f"\n{BOLD}Mages:{RESET}",)
    # for mage in mages:
    #     print(f"- {mage['name']} ({mage['power']} power)")

    # stats = mage_stats(mages)

    # print(f"\n{BOLD}Mage stats:{RESET}",)
    # for key, value in stats.items():
    #     print(f"- {key}: {value}")


# --- DEMO ---

def main() -> None:
    """Entry point of a program"""

    print(f"\n{BOLD}=== Lambda Sanctum ==={RESET}")

    # test data from generator

    artifacts = [
        {'name': 'Lightning Rod', 'power': 115, 'type': 'weapon'},
        {'name': 'Lightning Rod', 'power': 106, 'type': 'weapon'},
        {'name': 'Light Prism', 'power': 63, 'type': 'weapon'},
        {'name': 'Shadow Blade', 'power': 72, 'type': 'relic'}
    ]

    mages = [
        {'name': 'River', 'power': 78, 'element': 'light'},
        {'name': 'Ember', 'power': 66, 'element': 'light'},
        {'name': 'Alex', 'power': 81, 'element': 'earth'},
        {'name': 'Morgan', 'power': 97, 'element': 'water'},
        {'name': 'Casey', 'power': 60, 'element': 'light'}
    ]

    spells = [
        'tornado',
        'blizzard',
        'fireball',
        'heal'
    ]

    test_functions = {
        test_sorter: [artifacts],
        test_filter: [mages, 70],
        test_transformer: [spells],
        test_stats: [mages]
    }

    for function, arguments in test_functions.items():
        function(*arguments)
        print()
        print('-' * 40)

    print("\n✅ Lambda spells succesfully executed!\n")
    print('-' * 40)


if __name__ == "__main__":
    main()
