# Parrot Message Log

> *Your parrot never forgets a word. Say things, clear the deck, and ask the parrot to repeat the whole tale. Run `python main.py` and watch him squawk it all again.*

**Day 1 of "Building Aarakocras Madness"**, a series of small, standalone, pirate-themed Python tools by **Cpt. Dirtycode**.

- **Level:** Beginner
- **Type:** Extracted from Aarakocras Madness
- **Dependencies:** none (Python standard library only)

---

## Repository Purpose

A tiny message log with three jobs:

| Function  | What it does                                          |
|-----------|-------------------------------------------------------|
| `say()`   | Prints a line **and** stores it in the history        |
| `clear()` | Wipes the visible output (the history stays!)         |
| `redraw()`| Replays everything the parrot remembers, oldest first |

Almost every text game, chat tool or command-line program needs a history. This is the smallest honest version of it.

## Concepts Learned

- Lists of tuples and `append`
- Tuples of different lengths: `(message, color)` and `(name, message, color)`
- Unpacking tuples in a `for` loop
- Separating **storing** a message from **showing** it
- Why "clearing the screen" and "forgetting the history" are two different things

## Installation

You only need Python 3.8 or newer. There is nothing to install.

```bash
git clone https://github.com/<your-name>/parrot-message-log.git
cd parrot-message-log
```

## Usage

```bash
python main.py
```

The demo does four things:

1. Adds several example messages.
2. Shows the message history.
3. Clears the display.
4. Replays the full history.

## Example Output

```text
--- 1. The parrot starts talking (say + remember) ---
Squawk! Welcome aboard, landlubber.
Parrot: Pieces of eight! Pieces of eight!
The ship creaks and the sea smells of old socks.
Cook: Dinner is fish. Again.

--- 2. The parrot remembers 4 messages ---
(They were printed above and stored in message_history.)

--- 3. Clear the visible screen ---

============================================
   *** The deck has been scrubbed clean ***
============================================

--- 4. Replay the full history (redraw) ---
Squawk! Welcome aboard, landlubber.
Parrot: Pieces of eight! Pieces of eight!
The ship creaks and the sea smells of old socks.
Cook: Dinner is fish. Again.

Done! The history still holds 4 messages.
```

## Extracted From Aarakocras Madness

This tool is a console rebuild of the message system in Aarakocras Madness

| In the game            | In this repo                                        |
|------------------------|-----------------------------------------------------|
| `say()`                | `say()` and `say_as()`                              |
| `story_lines`          | `message_history`                                   |
| `clear_text()`         | `clear()`                                           |
| `redraw_story()`       | `redraw()`                                          |

What was removed or replaced:

- The PySide6 window calls (`window.append_story`, `window.clear_story`) became plain `print`.
- The Tk-style text widget calls (`text.configure`, `text.delete("1.0", tk.END)`) became a printed divider.
- One deliberate difference: the game's `clear_text()` also empties its list. Here `clear()` only wipes the *visible* output, so the demo can replay the full history afterwards.

## Future Improvement Ideas

- Give every speaker a real terminal color (see the next repo in the series, `crew-color-palette`).
- Add a `max_lines` limit so the history cannot grow forever.
- Save the history to a file and load it again later.
- Add a timestamp to every message.
- Add a small `unittest` file for `say`, `clear` and `redraw`.

---

*# Cpt. Dirtycode: The parrot repeats everything. That is not a bug, that is his whole personality.*
