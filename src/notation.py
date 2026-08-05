
def calculate_note_lengths(bpm):
    """Calculates note lengths in seconds"""
    quarter =60 / bpm
    note_values = {
        "whole": quarter * 4,
        "half": quarter * 2,
        "quarter": quarter,
        "eighth": quarter / 2,
        "sixteenth": quarter / 4,
    }
    return note_values


def determine_note_value(duration, note_lengths):
    smallest_difference = float("inf")

    best_note = None
    for note_type, length in note_lengths.items():
        current_difference = abs(length - duration)
        if current_difference <= smallest_difference:
            smallest_difference = current_difference
            best_note = note_type, length

    return best_note

