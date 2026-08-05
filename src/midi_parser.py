import pretty_midi
from pathlib import Path
def read_midi(file_path):
    project_root = Path(__file__).parent.parent
    midi_path = project_root/"midi"/file_path
    midi_data = pretty_midi.PrettyMIDI(midi_path)
    instrument = midi_data.instruments[0]
    print(instrument)

    notes = []

    for note in instrument.notes:
        note_info = {
            "pitch": pretty_midi.note_number_to_name(note.pitch),
            "start": float(note.start),
            "end": float(note.end),
            "duration": float(note.end - note.start),
            "velocity": note.velocity
        }

        notes.append(note_info)

    tempo_times, tempos = midi_data.get_tempo_changes()
    bpm = round(tempos[0])

    return notes, bpm

#Not Needed Later on
notes, bpm = read_midi("twinkle.mid")

for note in notes:
    print(note)
