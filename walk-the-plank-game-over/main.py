
# Cpt. Dirtycode: Every ending needs a "play again?" or the captain just stares at the sea forever.

import sys

# The captain's list of silly deeds. It starts empty on every new voyage.
achievements = []


def add_achievement(title):
    """Write a new deed into the list."""
    achievements.append(title)


def show_achievements():
    """Print every deed the crew earned on this voyage."""
    print("Deeds written in the captain's log:")
    if len(achievements) == 0:
        print("  (nothing, the log is as empty as the rum barrel)")
    for title in achievements:
        print("  *", title)


def game_over(reason):
    """Show the end screen. Every ending in this game walks through here."""
    print()
    print("==============================")
    print("         GAME OVER")
    print("==============================")
    print(reason)
    print()
    show_achievements()
    print()


def coming_soon():
    """A teaser ending. It shares the same game over screen as every other ending."""
    print()
    print("You found the secret passage! It leads to...")
    print("...a door with a sign: 'Closed for renovation. Back soon. - The Captain'")
    add_achievement("Found A Door That Is Not Finished Yet")
    game_over("The rest of the story is still being built. Come back later, matey!")


def start_adventure():
    """Play one short voyage. Every path ends in game_over()."""
    print()
    print("You stand on the deck of the Salty Parrot. The crew is staring at you.")
    print("What do you do?")
    print("  1) Walk the plank, just to see what happens")
    print("  2) Challenge the sea monster to a duel")
    print("  3) Look for the secret passage")

    choice = input("> ").strip()

    if choice == "1":
        add_achievement("Walked The Plank On Purpose")
        game_over("You took one step too many. The sea says hello. Glug.")
    elif choice == "2":
        add_achievement("Lost A Staring Contest With A Sea Monster")
        game_over("The monster blinked last. You blinked first. It was not close.")
    elif choice == "3":
        coming_soon()
    else:
        add_achievement("Could Not Read The Menu")
        game_over("You shouted something nobody understood and fell off the ship anyway.")


def play_again():
    """Ask the player about a new voyage. Returns True for yes and False for no."""
    while True:
        try:
            answer = input("Sail again? (yes/no) ").lower().strip()
        except EOFError:
            # Nobody is typing anymore, so the ship stays in the harbor.
            answer = "no"

        if answer in ("yes", "y"):
            achievements.clear()  # A new voyage starts with a clean log.
            print("Back to the deck, you stubborn legend!")
            return True
        if answer in ("no", "n"):
            print("Fair winds, sailor. The plank will wait for you.")
            return False

        print("That is neither a yes nor a no. The parrot is confused.")


def main():
    print("~~ WALK THE PLANK ~~")
    print("A very short voyage with a very dramatic ending.")

    while True:
        start_adventure()
        if not play_again():
            break

    sys.exit(0)


if __name__ == "__main__":
    main()
