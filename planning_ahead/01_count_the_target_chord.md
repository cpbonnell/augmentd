
# ========== Count the Target Cord ==========

Alejandro is working on a feature for the mobile app where users can filter for songs based on a specific chord. He wants to have one control where users can specify the notes of the chord, and another where they specify a percent. He will then filter songs to only look at those songs that have at least that percent of the song is that chord.

He would like you to write a function that he can use on the backend. You will be given a target chord (for example, "F A C E"), and a song (which will be a list of chords), and returns a number that is the count of how many times that chord shows up in the song. He can figure out the percentages on the front end.

For the sake of this feature, Alehandro says that all inversions of a chord and all voicings of a chord count as the same chord, but he does NOT want to consider extended chords to be the same. So "C E G" and "C E G B" are different, but "F A C E" and "F C F A E" are the same. Notes that are flatted or sharped will be denoted with a "b" or "#" respectively, and you may assume that a given song will never use two notations for the same note (that is, a song will either use "A#" or "Bb", but never both).


**Example:**
target = "F A C E"
song = ["F C A E", "F C F A C E", "F F F", "A C E"]

Answer: 2
Reason: FFF and ACE do not have all the notes of Fmaj7, so they do not count. But
the first two chords do.

**Example:**
target = "A C E"
song = ["C A E", "C A C E", "A C E G"]

Answer: 2
Reason: The first two chords of the song have all the required notes for the target
chord, but the last chord of the song contains the note G, which is not part of Adim.

```python

def count_target_chord(target: str, song: list[str]) -> int:
    # Hint: the key to solving this problem is that we care about whether a note
    # exists in a given chord, but we don't care about how many times it exists or
    # what order it's in. This lines up well with the Python data structure called
    # a Set. You can easily construct a set from a string or a list by calling the
    # constructor function:  set(my_str) of set(my_list)
    pass

```


Tests:
```python

# ========== Test the function ==========
target = "FACE"
song = ["FCAE", "FCFACE", "FFF", "ACE"]
answer = 2
your_answer = count_target_chord(target, song)
print(f"The correct answer is {answer}, and your answer is {your_answer}")

target = "ACE"
song = ["CAE", "CACE", "ACEG"]
answer = 2
your_answer = count_target_chord(target, song)
print(f"The correct answer is {answer}, and your answer is {your_answer}")

```