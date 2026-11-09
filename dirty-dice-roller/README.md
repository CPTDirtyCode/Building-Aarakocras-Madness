# Dirty Dice Roller

*Day 2 of Building Aarakocras Madness*

> Roll the Dirty Dice and let the sea decide. A 1 sinks you, a 20 makes you legend. Everything else is just wet.

## Purpose

Roll a d20 and turn the number into an outcome: a critical failure on 1, a critical success on 20, and a few bands in between. Every dragon fight in Aarakocras Madness is decided by a d20, and the captain decided that fate should be a function, not a coin flip hidden in the story.

## Concepts Learned

- `random.randint()` to roll a die
- `if / elif / else` chains
- Ordering conditions from most specific to least specific
- Simple function design (`roll_d20()` and `describe_roll(value)`)
- Separating game logic from display logic
- `random.seed()` to make a demo repeatable

## Installation

You only need Python 3. No extra packages, standard library only.

```bash
git clone https://github.com/<your-name>/dirty-dice-roller.git
cd dirty-dice-roller
```

## Usage

```bash
python main.py
```

The demo seeds the random generator and rolls the d20 ten times. Because of the seed, you get the same rolls every time.

| Roll | Outcome |
|------|---------|
| 1 | Critical failure |
| 2-5 | Terrible |
| 6-10 | Failure |
| 11-15 | Success |
| 16-19 | Great success |
| 20 | Critical success |

## Example Output

```
=== Cpt. Dirtycode's Dirty Dice Roller ===
Let the sea decide your fate!

Roll  1: [20] CRITICAL SUCCESS! The sea bows and the dragon hands you its hat.
Roll  2: [ 9] Failure. Everything is just wet and sad.
Roll  3: [12] Success! The crew nods with mild respect.
Roll  4: [17] Great success! Even the seagulls applaud.
Roll  5: [ 1] CRITICAL FAILURE! The mast snaps and the parrot files a complaint.
Roll  6: [15] Success! The crew nods with mild respect.
Roll  7: [ 8] Failure. Everything is just wet and sad.
Roll  8: [ 2] Terrible! Your cannon fires backwards.
Roll  9: [ 6] Failure. Everything is just wet and sad.
Roll 10: [ 4] Terrible! Your cannon fires backwards.

Yarr! The dice have spoken.
```

## Extracted From Aarakocras Madness

**Type: Extracted** from the game *Aarakocras Madness* (v0.8.5). The game rolls `random.randint(1, 20)` and then checks `== 20`, `> 10`, `> 1` and `== 1`, for example in the icy blizzard storm and the dragon finish choice. This repo lifts only that dice idea into a standalone tool. The story text, scene jumps and GUI calls are left out, and all pirate lines are new.

## Future Improvements

- Let the player type their own seed.
- Add a modifier, such as "roll with +3 Strength".
- Roll other dice (d6, d12) with a reusable `roll_die(sides)`.
- Count how often each outcome appears over many rolls.

---

*Part of the Building Aarakocras Madness journey. Fair winds, Cpt. Dirtycode.*
