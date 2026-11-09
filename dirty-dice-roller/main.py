# Cpt. Dirtycode: A natural 1 is not bad luck. It is the universe asking you to be more careful.
"""Dirty Dice Roller - Day 2 of Building Aarakocras Madness.

Roll a d20 and turn the number into a pirate-style outcome.
"""

import random

# The demo seed. Same seed = same rolls every time, so the output is repeatable.
DEMO_SEED = 5
NUMBER_OF_ROLLS = 10


# ---------------------------------------------------------------------------
# GAME LOGIC: these functions only roll and decide. They never print.
# ---------------------------------------------------------------------------

def roll_d20():
    """Roll one twenty-sided die and return a whole number from 1 to 20."""
    # randint includes BOTH ends, so 1 and 20 can both happen.
    return random.randint(1, 20)


def describe_roll(value):
    """Return a short pirate sentence for a d20 roll.

    Order matters: we check the most specific cases (1 and 20) first,
    then the wider ranges. The first matching branch wins.
    """
    if value == 1:
        return "CRITICAL FAILURE! The mast snaps and the parrot files a complaint."
    elif value == 20:
        return "CRITICAL SUCCESS! The sea bows and the dragon hands you its hat."
    elif value <= 5:
        return "Terrible! Your cannon fires backwards."
    elif value <= 10:
        return "Failure. Everything is just wet and sad."
    elif value <= 15:
        return "Success! The crew nods with mild respect."
    else:
        return "Great success! Even the seagulls applaud."


# ---------------------------------------------------------------------------
# DISPLAY LOGIC: this function only prints. It does not roll or decide.
# ---------------------------------------------------------------------------

def show_roll(roll_number, value, description):
    """Print one roll in a nice pirate-style line."""
    print(f"Roll {roll_number:>2}: [{value:>2}] {description}")


def main():
    """Run the demo: seed the dice, roll several times and show each result."""
    print("=== Cpt. Dirtycode's Dirty Dice Roller ===")
    print("Let the sea decide your fate!\n")

    # Seeding makes the "random" numbers repeatable.
    random.seed(DEMO_SEED)

    for roll_number in range(1, NUMBER_OF_ROLLS + 1):
        value = roll_d20()                # logic
        description = describe_roll(value)  # logic
        show_roll(roll_number, value, description)  # display

    print("\nYarr! The dice have spoken.")


if __name__ == "__main__":
    main()
