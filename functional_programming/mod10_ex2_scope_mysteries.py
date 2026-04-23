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


def mage_counter() -> callable:
    """Counting closure: return a function that
    counts how many times it has been called"""
    count = 0

    def counter() -> int:
        nonlocal count  # use variable from outside this function
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    """Return a function that accumulates power over time
    Each call adds the given amount to the total power"""
    total_power = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal total_power
        total_power += power_to_add
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    """Return a function that applies the specified enchantment.
    The returned function takes an item name and returns enchanted description.
    Format: "enchantment_type item_name" (e.g., "Flaming Sword")"""

    def enchanter(item: str) -> str:
        return (f"{enchantment_type} {item}")

    return enchanter  # can be lambda


def memory_vault() -> dict[str, callable]:
    """
    Memory management system.
    Return a dict with 'store' and 'recall' functions.
    'store' function: takes (key, value) and stores the memory
    'recall' function: takes (key) and returns stored value
    or "Memory not found"
    """

    memory = {}

    def store(key: any, value: any) -> None:
        memory[key] = value

    def recall(key: any) -> any:
        if key in memory:
            return memory[key]

        return "Memory not found"

    return {
        'store': store,
        'recall': recall
    }


# --- DEMO ---

def main() -> None:
    """Entry point of a program"""

    print(f"\n{BOLD}=== Scope Mysteries ==={RESET}")

    print(f"\n{ITALIC}{YELLOW}>> Testing mage counter...{RESET}\n")
    counter = mage_counter()
    for count in range(1, 4):
        print(f"- Call {count}: {counter()}")

    print('-' * 40)

    print(f"\n{ITALIC}{YELLOW}>> Testing spell accumulator...{RESET}\n")

    total_power = spell_accumulator(0)
    for power in range(1, 5):
        print(f"- Total power ({total_power(0)}) + {power} "
              f"= {total_power(power)}")

    print('-' * 40)

    print(f"\n{ITALIC}{YELLOW}>> Testing enchantment factory...{RESET}\n")

    enchantment1 = enchantment_factory('Flaming')
    enchantment2 = enchantment_factory('Frozen')
    items = ['Sword', 'Shield']

    for item in items:
        print(f"- {item} >> {ITALIC}enchanted with 🔥 Flame{RESET} >> "
              f"{enchantment1(item)}")
        print(f"- {item} >> {ITALIC}enchanted with 🧊 Ice{RESET} >> "
              f"{enchantment2(item)}")

    print('-' * 40)

    print(f"\n{ITALIC}{YELLOW}>> Testing memory management system...{RESET}\n")
    memory = memory_vault()
    items = {
        'sword': 'SWORD',
        'shield': 'SHIELD'
    }

    for key, value in items.items():
        print(f"- store '{key}'")
        memory['store'](key, value)
        print(f"- recall '{key}': {memory['recall'](key)}")

    print(f"\n- recall 'invalid': {memory['recall']('invalid')}")

    print('-' * 40)
    print("\n✅ Memory depths scoped!")
    print('-' * 40)


if __name__ == "__main__":
    main()
