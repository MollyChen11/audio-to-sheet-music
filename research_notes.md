Calculating Duration of Notes:
- Whole Note: 240/BPM seconds
- Half Note: 120/BPM seconds
- Quarter Note: 60/BPM seconds
- Quarter Note Triplet: 40/BPM seconds
- Eighth Note: 30/BPM seconds
- Eighth Note Triplet: 20/BPM seconds
- Sixteenth Note: 15/BPM seconds
-----------------------------------------------------------------------
beat_length = 60 / bpm

whole = beat_length * 4
half = beat_length * 2
quarter = beat_length
eighth = beat_length / 2
sixteenth = beat_length / 4

quarter_triplet = beat_length * (2/3)
eighth_triplet = beat_length / 3

-----------------------------------------------------------------------
Determining Note Values
1. Calculate one beat using beat_length = 60/bpm

2. Build note durations from beat_length

3. Compare the detected duration with each standard note value and choose the one that is the most similar.

_______________________________________________________________________
Things To Research
- Dotted Notes
- Ties
- Slurs
- Time Signatures
- Rests
- Articulation
- Dynamics
- Ornaments
- Determining Tempo
-----------------------------------------------------------------------
Future Ideas
- Wav to MIDI conversion
- Live microphone
- Dynamics using velocity
- Detecting articulations
- Choosing fingerings (Not as important)
- Tempo can be chosen by both user(version1) and computer(version2):
Select Input

1. MIDI File
2. WAV Recording

Choice: 2

Estimated tempo: 117 BPM

Would you like to:
1. Use 117 BPM
2. Enter your own tempo
-----------------------------------------------------------------------
Questions
- How to detect pickups
- How to implement and detect tempo changes
- How to store tempo in MIDI

-----------------------------------------------------------------------
Problems:
- Note value detection is inaccurate due to early releases, and articulation


