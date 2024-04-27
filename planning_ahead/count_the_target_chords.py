

# Count the Chords: You are given a target chord, and a song.
# Your task is to count the number of times that target chord appears in the
# song. We do NOT count Cmaj and Cmaj7 as the same chord, but we do count all
# inversions and voicings of a given chord as the same chord. So "CEG", "GCE",
# and "CGCEG" all count as Cmaj, but "CEGB" does not. For simplicity, all notes
# of the chord and the song will be in the key of C Major.

"""
Example:
target = "FACE"
song = ["FCAE", "FCFACE", "FFF", "ACE"]

Answer: 2
Reason: FFF and ACE do not have all the notes of Fmaj7, so they do not count. But
the first two chords do.
"""

"""
Example:
target = "ACE"
song = ["CAE", "CACE", "ACEG"]

Answer: 2
Reason: The first two chords of the song have all the required notes for the target
chord, but the last chord of the song contains the note G, which is not part of Adim.
"""

def count_target_chord(target: str, song: list[str]) -> int:
    # Hint: the key to solving this problem is that we care about whether a note
    # exists in a given chord, but we don't care about how many times it exists or
    # what order it's in. This lines up well with the Python data structure called
    # a Set. You can easily construct a set from a string or a list by calling the
    # constructor function:  set(my_str) of set(my_list)
    pass


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
