"""Configuration management for the Music Compositor"""

import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()

class Config:
    """Base configuration class"""
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', '')
    MODEL_NAME: str = os.getenv('MODEL_NAME', 'gpt-4o-mini')
    TEMPERATURE: float = float(os.getenv('TEMPERATURE', '0.7'))
    MAX_TOKENS: int = int(os.getenv('MAX_TOKENS', '2000'))
    
    # Audio Configuration
    AUDIO_FORMAT: str = os.getenv('AUDIO_FORMAT', 'wav')
    SAMPLE_RATE: int = int(os.getenv('SAMPLE_RATE', '44100'))
    DEFAULT_TEMPO: int = 60
    DEFAULT_DURATION: int = 8  # beats
    
    # Musical Scales and Chords
    SCALES = {
        'C major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'C minor': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
        'C harmonic minor': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
        'C melodic minor': ['C', 'D', 'Eb', 'F', 'G', 'A', 'B'],
        'C dorian': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
        'C phrygian': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'],
        'C lydian': ['C', 'D', 'E', 'F#', 'G', 'A', 'B'],
        'C mixolydian': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
        'C locrian': ['C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'],
        'C whole tone': ['C', 'D', 'E', 'F#', 'G#', 'A#'],
        'C diminished': ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'A', 'B'],
    }
    
    CHORDS = {
        'C major': ['C4', 'E4', 'G4'],
        'C minor': ['C4', 'Eb4', 'G4'],
        'C diminished': ['C4', 'Eb4', 'Gb4'],
        'C augmented': ['C4', 'E4', 'G#4'],
        'C dominant 7th': ['C4', 'E4', 'G4', 'Bb4'],
        'C major 7th': ['C4', 'E4', 'G4', 'B4'],
        'C minor 7th': ['C4', 'Eb4', 'G4', 'Bb4'],
        'C half-diminished 7th': ['C4', 'Eb4', 'Gb4', 'Bb4'],
        'C fully diminished 7th': ['C4', 'Eb4', 'Gb4', 'A4'],
    }
    
    MUSICAL_STYLES = [
        "Classical", "Romantic era", "Jazz", "Blues", "Rock", "Pop",
        "Electronic", "Ambient", "Folk", "Heavy Metal", "Hip Hop",
        "Country", "R&B", "Reggae", "Latin"
    ]
    
    INSTRUMENTS = [
        "Piano", "Guitar", "Violin", "Flute", "Trumpet",
        "Cello", "Drums", "Synthesizer", "Harp", "Organ"
    ]
    
    KEYS = [
        "C major", "C minor", "C# major", "D major", "D minor",
        "Eb major", "E major", "E minor", "F major", "F# major",
        "G major", "G minor", "Ab major", "A major", "A minor",
        "Bb major", "B major", "B minor"
    ]
    
    @classmethod
    def validate(cls) -> bool:
        """Validate configuration"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set. Please set it in .env file")
        return True

config = Config()
