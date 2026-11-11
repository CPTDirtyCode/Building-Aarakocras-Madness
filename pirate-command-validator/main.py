# Cpt. Dirtycode:
# The crew types all kinds of nonsense.
# Our job is to understand what they MEANT.

"""Pirate Command Validator.

A beginner-friendly demo of input cleaning and validation:
lower(), strip(), sets, the "in" operator and a re-ask while loop.
"""

from typing import Collection


def clean_input(text: str) -> str:
    """Normalize user input.

    strip() removes spaces at the start and end,
    lower() turns every letter into lowercase.
    Example: " YES " -> "yes"
    """
    return text.strip().lower()


def is_valid_choice(answer: str, choices: Collection[str]) -> bool:
    """Return True if the cleaned answer is one of the valid choices."""
    # "in" checks membership. On a set this check is fast and easy to read.
    return answer in choices


def ask_until_valid(prompt: str, choices: Collection[str]) -> str:
    """Keep asking until the user enters a valid choice, then return it."""
    print(prompt)

    # The loop only ends through "return", i.e. when the answer is valid.
    while True:
        answer = clean_input(input("> "))

        # Reject empty input first (nothing left after cleaning).
        if answer == "":
            print("The quartermaster stares at you in silence.")
            print("Even the parrot says more than that. Try again!")
            continue

        # Reject anything that is not in the set of valid choices.
        if not is_valid_choice(answer, choices):
            print("The quartermaster squints at you.")
            print("That answer belongs at the bottom of the sea.")
            continue

        print("Accepted, matey!")
        return answer


def main() -> None:
    """Run three demo scenarios that use ask_until_valid()."""
    print("Ahoy! The crew awaits your command.\n")

    # Scenario 1: yes/no question. Sets hold the valid answers.
    yes_answers = {"yes", "y"}
    no_answers = {"no", "n"}
    answer = ask_until_valid(
        "Do you want to raise the sails? (yes/no)",
        yes_answers | no_answers,  # union of both sets
    )
    if answer in yes_answers:
        print("Full speed ahead!\n")
    else:
        print("The ship remains in harbor.\n")

    # Scenario 2: choose a direction.
    direction = ask_until_valid(
        "Choose a direction. (left/right)",
        {"left", "right"},
    )
    print(f"The ship turns {direction}!\n")

    # Scenario 3: choose a ship role.
    role = ask_until_valid(
        "Choose a ship role. (captain/navigator/cook/gunner)",
        {"captain", "navigator", "cook", "gunner"},
    )
    print(f"You are now the ship's {role}. The crew salutes you!")


if __name__ == "__main__":
    main()
