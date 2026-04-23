#!/usr/bin/env python3

from functools import reduce, partial, lru_cache, singledispatch
import operator

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


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using selected operation."""

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")

    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """Create specialized enchantments using partial application."""

    fire = partial(base_enchantment, 50, 'fire')
    ice = partial(base_enchantment, 50, 'ice')
    lightning = partial(base_enchantment, 50, 'lightning')

    return {
        'fire_enchant': fire,
        'ice_enchant': ice,
        'lightning_enchant': lightning
    }


# memoization = keeping the function results in cache
# recursion and repeated calls

# LRU = Least Recently Used
# discarding LRU values from the cache if full

@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using memoization."""

    if n < 0:
        raise ValueError("n must be non-negative")

    if n in (0, 1):
        return n

    return (memoized_fibonacci(n - 1)
            + memoized_fibonacci(n - 2))


def spell_dispatcher() -> callable:
    """Create a single-dispatch spell system."""

    @singledispatch
    def spell(arg):
        return f"Default spell:\t{arg}"

    @spell.register(int)
    def damage_spell(arg):
        return f"Damage spell:\t{arg} power"

    @spell.register(str)
    def enchant_spell(arg):
        return f"Enchantment:\t{arg}"

    @spell.register(list)
    def multi_spell(arg):
        results = [spell(a) for a in arg]
        return f"Multi-cast:\n{"\n".join(results)}"

    return spell


# --- DEMO ---

def main() -> None:
    """Entry point of a program"""

    print(f"\n{BOLD}=== Functools artifacts ==={RESET}")

    # Spell Reducer

    print(f"\n{ITALIC}{YELLOW}>> Testing spell reducer...{RESET}\n")

    spell_powers = [33, 22, 12, 27, 50, 45]
    operations = ['add', 'multiply', 'max', 'min']

    print(f"Spell powers:  {spell_powers}\n")

    for operation in operations:
        print(f"- {operation.capitalize()}:  "
              f"{spell_reducer(spell_powers, operation)}")

    print('-' * 40)

    # Partial Enchanter

    print(f"\n{ITALIC}{YELLOW}>> Testing partial_enchanter...{RESET}\n")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"Enchanting {target} with {power} {element} power!"

    enchants = partial_enchanter(base_enchantment)

    fire = enchants["fire_enchant"]
    ice = enchants["ice_enchant"]
    lightning = enchants["lightning_enchant"]

    print(fire("Goblin"))
    print(ice("Troll"))
    print(lightning("Dragon"))

    print('-' * 40)

    # Fibonacci

    print(f"\n{ITALIC}{YELLOW}>> Testing memoized fibonacci...{RESET}\n")

    fibonacci_tests = [10, 11, 12, 10]

    for test in fibonacci_tests:
        print(f"- Fibonacci({test}):  {memoized_fibonacci(test)}")

    print('-' * 40)

    # Dispatcher

    print(f"\n{ITALIC}{YELLOW}>> Testing spell dispatcher...{RESET}\n")

    spell = spell_dispatcher()

    for typ, func in spell.registry.items():
        if typ is object:  # default func
            continue
        if typ is int:
            test_val = 42
        elif typ is str:
            test_val = "fire"
        elif typ is list:
            test_val = ["fireball", "heal", 5, 0.0]
        else:
            test_val = None
        print(f"- Testing {func.__name__} with {test_val}:\n"
              f"{func(test_val)}\n")

    print('-' * 40)
    print("\n✅ Functool artifacts managed!\n")
    print('-' * 40)


if __name__ == "__main__":
    main()
