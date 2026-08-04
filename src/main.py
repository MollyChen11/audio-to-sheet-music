from midi_parser import read_midi
from notation import create_sheet_music
from pathlib import Path
def main():
    print("Music Transcriber Started!")
    project_root = Path(__file__).parent.parent
    audio_path = project_root / "audio" / "c_major_scale.wav"

    notes = read_midi("twinkle.mid")
    #create_sheet_music(notes)


if __name__ == "__main__":
    main()