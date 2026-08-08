from midi_parser import read_midi
from notation import determine_rhythmic_duration
from pathlib import Path
def main():
    print("Music Transcriber Started!")
    project_root = Path(__file__).parent.parent
    audio_path = project_root / "audio" / "c_major_scale.wav"

    notes, bpm = read_midi("twinkle.mid")
    notes_value = determine_rhythmic_duration(notes, bpm)
    for note in notes_value:
        print(note["pitch"], note["duration"], note["note_value"])

if __name__ == "__main__":
    main()