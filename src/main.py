import librosa
import librosa.display
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np


def main():
    print("Music Transcriber Started!")

    # Load audio file
    project_root = Path(__file__).parent.parent
    audio_path = project_root/"audio"/"c_major_scale.wav "


    audio_data, sample_rate = librosa.load(audio_path)

    # Compute Short Time Fourier Transform
    # Finds frequencies present in small sections of the recording
    spectrum = librosa.stft(audio_data)

    # Converts frequency strengths to decibels for visualization
    spectrum_db = librosa.amplitude_to_db(abs(spectrum), ref=np.max)

    # Display Spectrogram
    librosa.display.specshow(
        spectrum_db,
        sr=sample_rate,
        x_axis="time",
        y_axis="hz"
    )

    # Labels for spectrogram
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")
    plt.xlabel("Time")
    plt.ylabel("Hertz")
    plt.ylim(0, 3000)
    plt.show()

    print(f"Sample rate: {sample_rate}")
    print(f"Number of samples: {len(audio_data)}")

    plt.plot(audio_data[61000:])
    plt.show()

if __name__ == "__main__":
    main()