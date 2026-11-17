# Walk-the-Plank Game Over Screen

Death is only the plank. Walk it with style.

A tiny pirate game for the terminal. You stand on the deck of the *Salty Parrot* and make one choice. Every choice ends the voyage with a proper "Game Over" screen, a list of your silly deeds, and a polite question: *Sail again?*

## Features

- Three choices on the deck, and every one ends in the same game over screen
- A captain's log that lists the deeds you earned during the voyage
- A "Sail again?" question that understands `yes`, `y`, `no` and `n` (big letters and extra spaces are fine)
- A friendly complaint from the parrot if you type something else
- A fresh, empty log at the start of every new voyage
- One clean exit when you answer "no"

## How To Run

You only need Python 3. There is nothing to install.

```
python main.py
```

## Example Usage

Here is one short play session. The lines after `>` and after `(yes/no)` are typed by the player.

```
~~ WALK THE PLANK ~~
A very short voyage with a very dramatic ending.

You stand on the deck of the Salty Parrot. The crew is staring at you.
What do you do?
  1) Walk the plank, just to see what happens
  2) Challenge the sea monster to a duel
  3) Look for the secret passage
> 1

==============================
         GAME OVER
==============================
You took one step too many. The sea says hello. Glug.

Deeds written in the captain's log:
  * Walked The Plank On Purpose

Sail again? (yes/no) maybe
That is neither a yes nor a no. The parrot is confused.
Sail again? (yes/no) yes
Back to the deck, you stubborn legend!

You stand on the deck of the Salty Parrot. The crew is staring at you.
What do you do?
  1) Walk the plank, just to see what happens
  2) Challenge the sea monster to a duel
  3) Look for the secret passage
> 3

You found the secret passage! It leads to...
...a door with a sign: 'Closed for renovation. Back soon. - The Captain'

==============================
         GAME OVER
==============================
The rest of the story is still being built. Come back later, matey!

Deeds written in the captain's log:
  * Found A Door That Is Not Finished Yet

Sail again? (yes/no) no
Fair winds, sailor. The plank will wait for you.
```

## What A Beginner Can Learn From It

- **Functions that call other functions.** `start_adventure()` calls `game_over()`, and `coming_soon()` also calls `game_over()`. The end screen is written only once.
- **A list that remembers things.** The `achievements` list keeps your deeds, and `clear()` empties it for a new voyage.
- **Returning a value.** `play_again()` returns `True` or `False`, and the main loop uses it to decide what happens next.
- **A loop that repeats until you are done.** The `while` loops in `main()` and `play_again()` keep going until there is a good answer.
- **Cleaning input.** `lower()` and `strip()` make `" YES "` work like `"yes"`.
- **A safe start point.** `if __name__ == "__main__":` lets the file run directly.

## Project Files

- `main.py` - the whole game
- `README.md` - this file
- `.gitignore` - tells Git to skip temporary files

## Ideas To Try Next

- Add more choices on the deck
- Show how many voyages you played
- Save your best list of deeds in a file

Happy sailing, and mind the plank!
