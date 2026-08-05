from midi_parser import read_midi
from notation import calculate_note_lengths, determine_note_value
from pathlib import Path
def main():
    print("Music Transcriber Started!")
    project_root = Path(__file__).parent.parent
    audio_path = project_root / "audio" / "c_major_scale.wav"

    notes, bpm = read_midi("twinkle.mid")
    note_lengths = calculate_note_lengths(bpm)
    for note in notes:
        note["note_value"] = determine_note_value(
            note["duration"],
            note_lengths
        )
        print(note["pitch"], note["duration"], note["note_value"])

    print(bpm)
    print(notes[0])


if __name__ == "__main__":
    main()