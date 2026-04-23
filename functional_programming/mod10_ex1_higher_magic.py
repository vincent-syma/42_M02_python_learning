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


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Combine two spells.
    Return function that calls both spells with the same arguments"""

    def combined(*args, **kwargs) -> tuple[any, any]:
        return spell1(*args, **kwargs), spell2(*args, **kwargs)

    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Amplify spell power.
    Return a new function that multiplies the base spell's result
    by multiplier"""

    def multiplied(*args, **kwargs) -> int:
        return base_spell(*args, **kwargs) * multiplier

    return multiplied


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Cast spell conditionally.
    Return a function that only casts the spell if condition returns True"""

    def conditioned_spell(*args, **kwargs) -> any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return conditioned_spell


def spell_sequence(spells: list[callable]) -> callable:
    """Create spell sequence.
    Return a function that casts all spells in order"""

    def sequence(*args, **kwargs) -> list[any]:
        return [spell(*args, **kwargs) for spell in spells]

    return sequence


# --- test functions ---

def heal(amount, target):
    return f"✨ Healing {target} for {amount} HP"


def fireball(power, target):
    return f"🔥 Fireball hits {target} with {power} damage"


def test_combiner(power: int, target: str) -> None:

    print(f"{ITALIC}>> Testing spell combiner...{RESET}\n")

    combined = spell_combiner(fireball, heal)

    print(f"Combined spell result:\t{combined(power, target)}")


def test_amplifier(power: int, multiplier: int) -> None:

    print(f"{ITALIC}>> Testing power amplifier...{RESET}\n")

    def fireball_int(power):
        return power

    super_fireball = power_amplifier(fireball_int, multiplier)

    print(f"Fireball:\t\t{fireball_int(power)}")
    print(f"Super fireball:\t\t{super_fireball(power)}")


def test_conditioned(power: int, target: str) -> None:

    print(f"{ITALIC}>> Testing conditional casting...{RESET}\n")

    def condition(power, target) -> bool:
        if power and target:
            return True
        return False

    conditioned_heal = conditional_caster(condition, heal)

    print(f"Conditional casting:\t{conditioned_heal(power, target)}")


def test_sequence(power: int, target: str) -> None:

    print(f"{ITALIC}>> Testing spell sequence...{RESET}\n")

    sequence1 = spell_sequence([fireball, heal])
    sequence2 = spell_sequence([heal, fireball])

    print(f"Spell sequence 1:\t{sequence1(power, target)}")
    print(f"Spell sequence 2:\t{sequence2(power, target)}")


# --- DEMO ---

def main() -> None:
    """Entry point of a program"""

    print(f"\n{BOLD}=== Higher Magic ==={RESET}\n")

    test_combiner(12, 'Dragon')
    print('-' * 40)
    test_amplifier(17, 3)
    print('-' * 40)
    test_conditioned(20, 'Goblin')
    print('-' * 40)
    test_sequence(0, 'Wizard')
    print('-' * 40)

    print("\n✅ Higher magic succesfully executed!\n")
    # print('-' * 40)


if __name__ == "__main__":
    main()
