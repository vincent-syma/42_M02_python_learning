#!/usr/bin/env python3


def main() -> None:
    """
    Entry point of the achievement tracker program.
    """
    print("=== Achievement Tracker System ===")
    print()

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()

    print("=== Achievement Analytics ===")
    all = alice.union(bob, charlie)  # alice | bob | charlie
    print(f"All unique achievements: {all}")
    print(f"Total unique achievements: {len(all)}")
    print()

    common = alice.intersection(bob, charlie)  # alice & bob & charlie
    print(f"Common to all players: {common}")

    shared = (alice & bob) | (bob & charlie) | (charlie & alice)
    rare = all - shared
    print(f"Rare achievements (1 player): {rare}")

    print()

    a_b_common = alice.intersection(bob)
    print("=== Alice vs Bob ===")
    print(f"common: {a_b_common}")
    a_unique = alice.difference(bob)  # alice - bob - charlie
    print(f"Alice unique: {a_unique}")
    b_unique = bob.difference(alice)  # bob - alice - charlie
    print(f"Bob unique: {b_unique}")


if __name__ == "__main__":
    main()
