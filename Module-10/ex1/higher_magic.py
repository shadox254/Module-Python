from typing import Any, Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any):
        result_spell1 = spell1(*args, **kwargs)
        result_spell2 = spell2(*args, **kwargs)
        return (result_spell1, result_spell2)
    return wrapper


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def wrapper(*args: Any, **kwargs: Any):
        spell_power = base_spell(*args, **kwargs)
        new_power = spell_power * multiplier
        return new_power
    return wrapper


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any):
        if not condition(*args, **kwargs):
            return "Spell fizzled"
        return spell(*args, **kwargs)
    return wrapper


def spell_sequence(spells: list[callable]) -> callable:
    def wrapper(*args: Any, **kwargs: Any):
        result = []
        for spell in spells:
            result.append(spell(*args, **kwargs))
        return result
    return wrapper


def higher_magic():
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    target = "Dragon"
    combined = spell_combiner(fireball, heal)
    print(f"{combined(target)[0]}, {combined(target)[1]}")
    print()

    def fireball_spell(power: int) -> int:
        return power

    print("Testing power amplifier...")
    base_power = 10
    multiplier = 3
    mega_fireball = power_amplifier(fireball_spell, multiplier)
    print(f"Original: {base_power}, Amplified: {mega_fireball(base_power)}")
    print()

    def is_true(boolean: bool) -> bool:
        if not boolean:
            return False
        return True

    def spell(random: Any):
        return "Spell created"

    print("Testing conditionnal caster...")
    cond_caster = conditional_caster(is_true, spell)
    print(cond_caster(True))
    print()

    print("Testing spell sequence...")
    spells = [heal, fireball, heal]
    sequence = spell_sequence(spells)
    print(f"Casting spell sequence: {", ".join(sequence("Dragon"))}")
    print()


if __name__ == "__main__":
    higher_magic()
