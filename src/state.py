"""State definition for the music composition workflow"""

from typing import TypedDict
from dataclasses import dataclass

class MusicState(TypedDict):
    """Define the structure of the state for the music generation workflow."""
    musician_input: str      # User's input describing the desired music
    melody: str              # Generated melody
    harmony: str             # Generated harmony
    rhythm: str              # Generated rhythm
    style: str               # Desired musical style
    composition: str         # Complete musical composition
    midi_file: str           # Path to the generated MIDI file
    tempo: int               # Tempo in BPM
    key: str                 # Musical key
    instrument: str          # Instrument choice

@dataclass
class CompositionMetadata:
    """Metadata for a generated composition"""
    title: str
    artist: str
    style: str
    key: str
    tempo: int
    instrument: str
    duration_beats: int
    created_at: str
