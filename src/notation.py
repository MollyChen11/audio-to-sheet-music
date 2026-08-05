
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
