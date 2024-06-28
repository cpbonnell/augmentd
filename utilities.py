"""
Our goal today is to get to the point where we have a function takes two notes,
say "Bb" and "D", and returns the number of half-steps in between the them (in
this case, 4). The constraint (just for fun and learning), is that we will not
be allowed to hard-code anything, except for the list of notes which have no sharps.

We will likely want to build up to this final function by writing some smaller
"helper functions" first to solve small parts of this work for us. A good rule of
thumb for this exercise is that functions should be less than 10 lines long, probably
closer to 5.

We want the function to work correctly even if the second note
comes before the first note alphabetically (e.g. "G" and "D"). We also want to
make sure that the number of half steps is measured assuming that the first note
is the one lower in pitch. So `number_of_half_steps("G", "D")` should return 7 but
`number_of_half_steps("D", "G")` should return 5.
"""

from string import ascii_uppercase
NOTES_WITH_NO_SHARP = ["B", "E"]
NOTES_WITH_NO_FLAT = ["C", "F"]
SHARP_SYMBOL = "#"
FLAT_SYMBOL = "b"

def white_keys() -> list[str]:
    """
    Return a list with all names of the white keys on a keyboard, in alphabetic order.
    """
    all_letters = [s for s in ascii_uppercase]
    return all_letters[:7]

def black_keys_sharp() -> list[str]:
    """
    Return a list with all the names of the black keys on the keyboard as sharps
    """
    # white_keys_with_sharps
    pass




# Here is our big final function:
# def number_of_half_steps(lower: str, upper: str) -> int:
#     pass

if __name__ == "__main__":
    # Tests
    wk = white_keys()
    assert wk[0] == "A"
    assert wk[1] == "B"
    assert wk[6] == "G"
    assert "H" not in wk
    print("All tests for white_keys() passed!")

    # assert number_of_half_steps("G", "D") == 7
    # assert number_of_half_steps("Gb", "Db") == 7
    # assert number_of_half_steps("G#", "D#") == 7
    # assert number_of_half_steps("G#", "Db") == 5
    # assert number_of_half_steps("D", "G") == 7