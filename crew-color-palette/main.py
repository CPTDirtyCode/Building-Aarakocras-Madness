# Cpt. Dirtycode:
# Every pirate gets a voice color.
# Unknown sailors get the white color.
# Same as suspicious strangers at night.

"""Crew Color Palette.

A beginner-friendly demo of dictionaries used as lookup tables:
dict.get(), default values, ANSI terminal colors and the separation
of data (the dictionaries) from presentation (the printing).
"""

import os
from typing import Dict

# Data part 1: ANSI escape codes. Color name -> terminal code.
COLORS: Dict[str, str] = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
}

# The reset code switches the terminal back to its normal color.
# Without it, the whole rest of the terminal stays colored!
RESET = "\033[0m"

# Data part 2: who speaks in which color.
# It only stores color NAMES, not ANSI codes. Data stays separate.
CHARACTER_COLORS: Dict[str, str] = {
    "Captain": "red",
    "Navigator": "blue",
    "Cook": "green",
    "Parrot": "yellow",
    "Ghost": "cyan",
}

# The fallback for anyone who is not in the table.
DEFAULT_COLOR = "white"


def get_color(name: str) -> str:
    """Return the ANSI color code for a speaker.

    Unknown speakers get white instead of a KeyError.
    """
    # dict.get(key, default) returns the default when the key is missing.
    # CHARACTER_COLORS["Stranger"] would crash, .get() does not.
    color_name = CHARACTER_COLORS.get(name, DEFAULT_COLOR)
    return COLORS[color_name]


def npc(name: str, message: str) -> None:
    """Print a line like "[Captain]: Set sail!" with the name in color."""
    color_code = get_color(name)
    # The reset code comes right after the name, so only the name is colored.
    print(f"[{color_code}{name}{RESET}]: {message}")


def demo_conversation() -> None:
    """Show a short, silly pirate conversation."""
    npc("Captain", "Set sail! The treasure will not find itself!")
    npc("Navigator", "Captain, the map is upside down again.")
    npc("Cook", "Dinner is ready. Today's special: mystery stew.")
    npc("Parrot", "Mystery stew! Mystery stew! SQUAWK!")
    npc("Ghost", "Booo! ...Is the stew vegetarian?")
    # Cpt. Dirtycode: This sailor is not in the table. White it is.
    npc("Stranger", "Hello. Is this the ferry to Tortuga?")
    npc("Captain", "Nobody invited the Stranger. Who left the plank down?")
    npc("Mysterious Mermaid", "Just passing through. Love the stew.")
    npc("Parrot", "Stranger danger! SQUAWK!")


def main() -> None:
    """Prepare the terminal and run the demo."""
    # On Windows, an empty system call switches on ANSI color support.
    if os.name == "nt":
        os.system("")

    print("=== The Crew Speaks ===\n")
    demo_conversation()
    print("\n=== End of Conversation ===")


if __name__ == "__main__":
    main()
