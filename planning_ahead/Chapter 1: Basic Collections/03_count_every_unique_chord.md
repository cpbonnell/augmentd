
# ========== Count Every Unique Chord ==========

## Instructor Notes
1. Make sure the student knows about the following operations:
    - Use a `Dict` to map keys to values
    - use `defaultdict` for the pattern where the type of every value is known
2. The "hard version" of this problem requires knowing not just how many distinct chords there are in a song, but also identifying the unique voicings of each chord. This will require a dict mapping the string-key of each chord to a set, and then the set needs the raw chord as it was supplied.

## Problem
Alejandro is quite pleased with the work you did for ticket AGM-101. He says that the chord percentage feature has been quite well recieved! But now there is actually been some requests to take the chord breakdown a bit farther. Now, Jay wants a screen in the mobile app where a user can click on any given song, and see a breakdown of every unique chord used in the song, and how often it occurs. Alejandro has tried a solution where he calls your function from AGM-101 multiple times per song to get a number for every imaginable chord, but it takes far too long so he wants you to write a new function.

Franchesca has helpfully pointed out that this kind of chart is known as a "Histogram." But Jay doesn't see what it has to do with history, so he has decided to brand this specific screen as a the "Augment'd Song DNA Breakdown," and had the attorney file trademark paperwork.

Your task is to write a function that takes in a song (i.e. a list of strings indicating the notes being played), and returns a dictionary with unique chords as the keys. The value associated with each key should be the number of times that chord occurs in the song.

## Setup
```python
def count_for_every_unique_chord(song: list[str]) -> dict[str, int]:
    pass
```