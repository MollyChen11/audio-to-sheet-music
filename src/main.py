from midi_parser import read_midi
from notation import calculate_note_lengths
from pathlib import Path
def main():
    print("Music Transcriber Started!")
    project_root = Path(__file__).parent.parent
    audio_path = project_root / "audio" / "c_major_scale.wav"

    notes, bpm = read_midi("twinkle.mid")
    note_lengths = calculate_note_lengths(bpm)


if __name__ == "__main__":
    main()