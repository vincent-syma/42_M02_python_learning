#!/usr/bin/env python3

from functools import wraps

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


def spell_timer(func: callable) -> callable:
    """Decorator that times spell execution."""

    import time

    @wraps(func)  # keeping metadata from og function
    def timer(*args, **kwargs) -> any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return timer


def power_validator(min_power: int) -> callable:
    """Power validation decorator."""

    def decorator(func: callable) -> callable:
        @wraps(func)
        def validator(*args, **kwargs) -> any:
            if not args:  # not checking kwargs - kwargs.get("power")
                return func(*args, **kwargs)
            if len(args) >= 2 and hasattr(args[0], "__class__"):
                power = args[1]  # method
            else:
                power = args[0]
            if not isinstance(power, (int, float)):
                return "Power attribute missing or of invalid type"
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return validator

    return decorator


def retry_spell(max_attempts: int) -> callable:
    """Decorator that retries failed spells.
    If function raises an exception, retry up to max_attempts times."""

    def decorator(func: callable) -> callable:
        @wraps(func)
        def retry_spell(*args, **kwargs) -> any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")

            return "Spell casting failed after max_attempts attempts"

        return retry_spell

    return decorator


class MageGuild:
    """MageGuild class"""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Checks if name is valid.
        Name is valid if it's at least 3 characters
        and contains only letters/spaces"""
        return (len(name) >= 3 and
                all(char.isalpha() or char.isspace()
                    for char in name))

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"
    # I changed the order of the arguments because of the validator


# --- DEMO ---

def main() -> None:
    """Entry point of a program"""

    print(f"\n{BOLD}=== Master's Tower ==={RESET}")

    # Spell Timer

    print(f"\n{ITALIC}{YELLOW}>> Testing spell timer...{RESET}\n")

    @spell_timer
    def fireball(damage):
        for _ in range(damage):
            pass  # time simulation
        return "Fireball cast!"

    print(f"Result: {fireball(100000000)}")

    print('-' * 40)

    # Power Validator

    print(f"\n{ITALIC}{YELLOW}>> Testing power validator...{RESET}\n")

    @power_validator(min_power=16)
    def heal(amount):
        return f"Healing {amount} HP"

    test_powers = [20, 15, 17, 6]

    for power in test_powers:
        print(f"- Heal ({power}): {heal(power)}")

    print('-' * 40)

    # Retry Spell

    print(f"\n{ITALIC}{YELLOW}>> Testing retry spell...{RESET}\n")

    attempts = 0

    @retry_spell(max_attempts=3)
    def deterministic_spell():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("Spell fizzled!")
        return "Spell succeeded!"

    print(deterministic_spell())

    print('-' * 40)

    print(f"\n{ITALIC}{YELLOW}>> Testing MageGuild...{RESET}")

    mage_names = ['Zara', 'Riley', 'Pho enix', 'Ember']
    invalid_names = ['Jo', 'Alex123', 'Test@Name']

    guild = MageGuild()

    print(f"\n{BOLD}Validating mage names:{RESET}")
    for name in mage_names:
        print(f" - '{name}':\t{guild.validate_mage_name(name)}")

    print(f"\n{BOLD}Invalid mage names:{RESET}")
    for inv_name in invalid_names:
        print(f" - '{inv_name}':\t{guild.validate_mage_name(inv_name)}")

    print(f"\n{BOLD}Casting spells with validation:{RESET}")

    spell_names = ['flash', 'freeze', 'shield', 'darkness']

    for i in range(len(spell_names)):
        name = spell_names[i]
        power = test_powers[i]
        print(guild.cast_spell(power, name))

    print('-' * 40)
    print("\n✅ Master's Tower conquered with decorators!")
    print('-' * 40)


if __name__ == "__main__":
    main()
