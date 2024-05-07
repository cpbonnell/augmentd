# ========== Learning the Sliding Window approach ==========

## Instructor Notes
1. This problem will require combining both the sliding window technique, as well as the use of sets to look for unique items.


## Problem Context
Alejandro is working on a ranking system that recommends songs based on the guitar solo in that song. He needs you to write a function that identifies the longes riff in the guitar solo that does not contain any repeated chords.

For the sake of this task, all voicings and inversions of a chord are to be considered the same chord, but single notes are not considered a chord. To be considered a chord, the cluster of notes must have at least two distinct notes named. So "Eb G Bb D" and "Eb Eb D G Bb" are both considered the same chord (Ebmaj7), but "D" is not a chord, and neither is "D D" or "D D D". You may also assume that a song will always use the same notation for every note (e.g. a given song may use "Ab" or "G#", but never both).

**Setup**
```python
def longest_riff(song: list[str]) -> int:
    pass
```

**Test Cases**
```python
song = ["Eb Eb D G Bb", "G", "D", "G", "D", "Eb F Ab C Eb", "F", "C", "G Eb D Bb", "G", "D", "Eb", "Bb"]
answer = 9
print(f"The correct answer is {answer}, your answer is {longest_riff(song)}")
```