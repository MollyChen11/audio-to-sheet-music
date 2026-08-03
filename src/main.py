import librosa
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    print("Music Transcriber Started!")

    project_root = Path(__file__).parent.parent
    audio_path = project_root/"audio"/"flute_note.wav"

    audio_data, sample_rate = librosa.load(audio_path)

    print(f"Sample rate: {sample_rate}")
    print(f"Number of samples: {len(audio_data)}")

    plt.plot(audio_data[:500])
    plt.show()
if __name__ == "__main__":
    main()