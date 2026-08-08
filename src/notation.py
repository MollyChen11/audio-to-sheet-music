# Future improvements:
# Add dotted notes
# Add triplets
# Improve handling of last note
# Work with tempo changes
def calculate_note_lengths(bpm):
    """Calculates note lengths in seconds"""
    quarter = 60 / bpm
    note_values = {
        "whole": quarter * 4,
        "half": quarter * 2,
        "quarter": quarter,
        "eighth": quarter / 2,
        "sixteenth": quarter / 4,
    }

    return note_values

def determine_note_value(duration, note_lengths):
    """Determines the note value by calculating the difference between the start and end times and comparing it with each note value"""
    smallest_difference = float("inf")

    best_note = None
    for note_type, length in note_lengths.items():
        current_difference = abs(length - duration)
        if current_difference <= smallest_difference:
            smallest_difference = current_difference
            best_note = note_type, length

    return best_note

def determine_rhythmic_duration(notes, bpm):
    """Determines the rhythmic value of each note. Uses time between consecutive notes to calculate the duration."""

    note_lengths = calculate_note_lengths(bpm)

    for i in range(len(notes)):
        # Uses held duration as estimate, since last note has no following note
        if i == len(notes) - 1:
            rhythmic_duration = notes[i]["duration"]

        else:
            # Determines onset duration given the next note's start time
           rhythmic_duration = notes[i + 1]["start"] - notes[i]["start"]

        note_value = determine_note_value(rhythmic_duration, note_lengths)
        notes[i]["note_value"] = note_value

    return notes