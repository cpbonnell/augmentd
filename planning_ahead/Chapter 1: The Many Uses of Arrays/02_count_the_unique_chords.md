
# ========== Count the Unique Chords ==========

## Instructor Notes
1. Make sure the student knows about the following operations:
    - `sorted(my_set)` gives back a list in the sorted order
    - `"".join(my_list)` gives you a string with the elements of the list in order
    - You can use `len(set)` to tell how many items it has
2. This problem requires use of sets to determine the unique elements in a chord
3. It also requires a set to record which chords have been seen. But sets themselves are not hashable, so one has to convert the chord-set back to a string in a predictable order so it can be checked against other chords

## Problem
Franchesca, the resident data scientist, is working on a model to try and predict how "jazzy" a song is. She has heard from Jean Pierre that Jazz songs have more chords in them than "normal" songs, and so she wants to feed "number of unique chords" into her model as a feature. Your task is to write a function that will take a list of the note clusters played in a song, and returns the number of distinct chords present in that song.

For the sake of this feature, Franchesca says that all inversions of a chord and all voicings of a chord count as the same chord, but she does NOT want to consider extended chords to be the same. So "C E G" and "C E G B" are different, but "F A C E" and "F C F A E" are the same. Notes that are flatted or sharped will be denoted with a "b" or "#" respectively, and you may assume that a given song will never use two notations for the same note (that is, a song will either use "A#" or "Bb", but never both).

Example:
song = ["F A C E", "F C F A C E", "A C E", "F A C E G#"]

Answer: 3

Reason: The first two chords are the same, since they contain the exact same notes
even if they are in a different order or different quantity. But "A C E" is missing
the root, F, and the last chord has an added sharp 9, so we don't consider those to
be the same chord.

## ========== Setup ==========
```python

def count_of_unique_chords(song: list[str]) -> int:
    pass

```
