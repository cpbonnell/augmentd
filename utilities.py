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
    Return a list with all the names of the black keys on the keyboard as sharps.
    """
    keys_that_need_sharps = [x for x in white_keys() if x not in NOTES_WITH_NO_SHARP]
    keys_as_sharps = [x + SHARP_SYMBOL for x in keys_that_need_sharps]
    return keys_as_sharps


def black_keys_flat() -> list[str]:
    """
    Return a list with all the names of the black keys on the keyboard as flats starting on Bb.

    This list corresponds 1 to 1 with the list black_keys_sharp(). List indices are equivalent.
    """

    list_of_white_keys = white_keys()

    keys_that_are_sharps = [
        x for x in list_of_white_keys if x not in NOTES_WITH_NO_SHARP
    ]

    list_of_sharps_indices = [list_of_white_keys.index(x) for x in keys_that_are_sharps]

    list_of_flats_indices = [x + 1 for x in list_of_sharps_indices]

    two_octave_white_keys = list_of_white_keys * 2

    keys_that_need_flats = [two_octave_white_keys[x] for x in list_of_flats_indices]

    return [x + FLAT_SYMBOL for x in keys_that_need_flats]


def complete_octave_with_sharps() -> list[str]:
    """
    Return a list of the whole musical octave with the black keys represented as sharps.
    """
    return sorted(black_keys_sharp() + white_keys())


def convert_to_enharmonic_value(note: str) -> str:
    """
    Returns the equivalent sharp if given a flat, and returns the equivalent flat if given a sharp.
    If given a white key without a flat or sharp, returns the same key.
    """

    # TODO: Expand the function to include ALL flats and sharps whether or not they are actually black keys on the keyboard.

    if SHARP_SYMBOL in note:
        index_enharmonic = black_keys_sharp().index(note)
        all_flats = black_keys_flat()
        return all_flats[index_enharmonic]
    elif FLAT_SYMBOL in note:
        index_enharmonic = black_keys_flat().index(note)
        all_sharps = black_keys_sharp()
        return all_sharps[index_enharmonic]
    else:
        return note


def number_of_half_steps(lower: str, upper: str) -> int:
    """
    Returns the number of half steps between lower and upper notes, starting the count from lower and going up.

    Passing the same note for both lower and upper will return the value of an octave. Unison is excluded.
    """

    # TODO: Create a way for the function to distinguish octaves and return Unison as an output.

    two_octaves_with_sharps = (
        complete_octave_with_sharps() + complete_octave_with_sharps()
    )

    if FLAT_SYMBOL in lower:
        lower = convert_to_enharmonic_value(lower)
    if FLAT_SYMBOL in upper:
        upper = convert_to_enharmonic_value(upper)

    lower_index = two_octaves_with_sharps.index(lower)
    upper_index = two_octaves_with_sharps.index(upper, lower_index + 1)

    return upper_index - lower_index


if __name__ == "__main__":
    UNICODE_GREEN_CHECK = "\u2714"

    # Tests
    wk = white_keys()
    assert wk[0] == "A"
    assert wk[1] == "B"
    assert wk[6] == "G"
    assert "H" not in wk
    print(f"{UNICODE_GREEN_CHECK} All tests for white_keys() passed!")

    bks = black_keys_sharp()
    assert bks[0] == "A#"
    assert bks[1] == "C#"
    assert bks[4] == "G#"
    assert "A" not in bks
    assert all([note.endswith(SHARP_SYMBOL) for note in bks])
    assert all(["b" not in note for note in bks])
    print(f"{UNICODE_GREEN_CHECK} All tests for black_keys_sharp() passed!")

    bkf = black_keys_flat()
    assert bkf[0] == "Bb"
    assert bkf[1] == "Db"
    assert bkf[4] == "Ab"
    assert "Cb" not in bkf
    assert "Fb" not in bkf
    assert all([note.endswith(FLAT_SYMBOL) for note in bkf])
    assert all(["#" not in note for note in bkf])
    print(f"{UNICODE_GREEN_CHECK} All tests for black_keys_flat() passed!")

    assert convert_to_enharmonic_value("Db") == "C#"
    assert convert_to_enharmonic_value("Ab") == "G#"
    assert convert_to_enharmonic_value("D#") == "Eb"
    assert convert_to_enharmonic_value("D") == "D"
    assert convert_to_enharmonic_value("A") == "A"
    print(f"{UNICODE_GREEN_CHECK} convert_to_enharmonic_value() passed!")

    assert number_of_half_steps("G", "D") == 7
    assert number_of_half_steps("Gb", "Db") == 7
    assert number_of_half_steps("G#", "D#") == 7
    assert number_of_half_steps("G#", "Db") == 5
    assert number_of_half_steps("D", "G") == 5
    assert number_of_half_steps("A", "A") == 12
    assert number_of_half_steps("A", "A#") == 1
    assert number_of_half_steps("A", "Bb") == 1
    print(f"{UNICODE_GREEN_CHECK} number_of_half_steps() passed!")
