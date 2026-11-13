# Crew Color Palette

A beginner-friendly pirate-themed terminal utility. Every crew member has a voice color stored in a dictionary. Unknown speakers safely fall back to white instead of crashing the program.

## Features

- Speaker-to-color lookup table (`CHARACTER_COLORS`)
- Separate ANSI color table (`COLORS`)
- Safe fallback to white for unknown speakers using `dict.get()`
- Colored speaker names with proper ANSI reset codes
- A short, humorous pirate conversation demo

## Concepts Learned

- Dictionaries
- dict.get()
- ANSI Colors
- Functions
- Fallback Values

## How To Run

```
python main.py
```

Python Standard Library only. No external dependencies.

## Example Output

The names appear in color in a real terminal (shown here without color):

```
=== The Crew Speaks ===

[Captain]: Set sail! The treasure will not find itself!
[Navigator]: Captain, the map is upside down again.
[Cook]: Dinner is ready. Today's special: mystery stew.
[Parrot]: Mystery stew! Mystery stew! SQUAWK!
[Ghost]: Booo! ...Is the stew vegetarian?
[Stranger]: Hello. Is this the ferry to Tortuga?
[Captain]: Nobody invited the Stranger. Who left the plank down?
[Mysterious Mermaid]: Just passing through. Love the stew.
[Parrot]: Stranger danger! SQUAWK!

=== End of Conversation ===
```

Colors: Captain = red, Navigator = blue, Cook = green, Parrot = yellow, Ghost = cyan, Stranger and Mermaid = white (fallback).

## Future Ideas

- Load the crew colors from a JSON file
- Add bold and underline styles next to colors
- Let the user add new crew members while the program runs


The concept is extracted from Aarakocras Madness (the NPC color table and its white fallback).