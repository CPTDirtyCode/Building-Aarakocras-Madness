# Cpt. Dirtycode: The parrot repeats everything. That is not a bug, that is his whole personality.
"""
Parrot Message Log  (Day 1 of "Building Aarakocras Madness")

A tiny message log with three jobs:

    say()    -> show a line AND remember it
    clear()  -> wipe what is visible (the memory stays!)
    redraw() -> replay everything the parrot remembers

Only the Python standard library is used. Run it with:  python main.py
"""

# The parrot's memory: a list of tuples.
#   A plain line      is stored as  (message, color)
#   A line by a name  is stored as  (name, message, color)
# The tuples have different lengths on purpose, so redraw() can tell them
# apart by counting the items (just like the original game does).
message_history = []

# A divider is our "screen wipe". A real terminal cannot be un-printed, so we
# print a visible line instead of deleting anything.
DIVIDER = "=" * 44


def say(message, color="white"):
    """Show a plain message and remember it."""
    # Step 1: STORE the message in the history list.
    message_history.append((message, color))
    # Step 2: SHOW the message on the screen.
    print(message)


def say_as(name, message, color="white"):
    """Show a message spoken by a named character and remember it."""
    message_history.append((name, message, color))
    print(f"{name}: {message}")


def clear():
    """Wipe the visible output. The history list is NOT touched."""
    # Printing a divider and a few blank lines acts as our "clear screen".
    print()
    print(DIVIDER)
    print("   *** The deck has been scrubbed clean ***")
    print(DIVIDER)
    print()


def redraw():
    """Replay every remembered message, oldest first."""
    for entry in message_history:
        # len() tells us which tuple shape we have.
        if len(entry) == 2:
            # Unpacking: the two items go into two variables at once.
            message, color = entry
            print(message)
        else:
            name, message, color = entry
            print(f"{name}: {message}")
    # The color is stored but not used here. Colors come to life in the
    # next repository of the series (Crew Color Palette).


def main():
    """Demo: say some lines, show the history, clear, replay everything."""
    print("--- 1. The parrot starts talking (say + remember) ---")
    say("Squawk! Welcome aboard, landlubber.")
    say_as("Parrot", "Pieces of eight! Pieces of eight!", "green")
    say("The ship creaks and the sea smells of old socks.")
    say_as("Cook", "Dinner is fish. Again.", "yellow")

    print()
    print(f"--- 2. The parrot remembers {len(message_history)} messages ---")
    print("(They were printed above and stored in message_history.)")

    print()
    print("--- 3. Clear the visible screen ---")
    clear()

    print("--- 4. Replay the full history (redraw) ---")
    redraw()

    print()
    print(f"Done! The history still holds {len(message_history)} messages.")


if __name__ == "__main__":
    main()
