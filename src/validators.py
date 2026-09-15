"""Input validators for the Music Compositor"""

from typing import Dict, Any
from src.exceptions import InvalidInputError
from src.config import config

def validate_music_input(musician_input: str) -> bool:
    """Validate musician input"""
    if not isinstance(musician_input, str):
        raise InvalidInputError("musician_input must be a string")
    if len(musician_input) < 5:
        raise InvalidInputError("musician_input must be at least 5 characters")
    if len(musician_input) > 500:
        raise InvalidInputError("musician_input must not exceed 500 characters")
    return True

def validate_style(style: str) -> bool:
    """Validate musical style"""
    if not isinstance(style, str):
        raise InvalidInputError("style must be a string")
    if style not in config.MUSICAL_STYLES:
        raise InvalidInputError(f"style must be one of {config.MUSICAL_STYLES}")
    return True

def validate_key(key: str) -> bool:
    """Validate musical key"""
    if not isinstance(key, str):
        raise InvalidInputError("key must be a string")
    if key not in config.KEYS:
        raise InvalidInputError(f"key must be one of {config.KEYS}")
    return True

def validate_instrument(instrument: str) -> bool:
    """Validate instrument"""
    if not isinstance(instrument, str):
        raise InvalidInputError("instrument must be a string")
    if instrument not in config.INSTRUMENTS:
        raise InvalidInputError(f"instrument must be one of {config.INSTRUMENTS}")
    return True

def validate_tempo(tempo: int) -> bool:
    """Validate tempo"""
    if not isinstance(tempo, int):
        raise InvalidInputError("tempo must be an integer")
    if tempo < 40 or tempo > 180:
        raise InvalidInputError("tempo must be between 40 and 180 BPM")
    return True

def validate_duration(duration: int) -> bool:
    """Validate duration"""
    if not isinstance(duration, int):
        raise InvalidInputError("duration must be an integer")
    if duration < 4 or duration > 32:
        raise InvalidInputError("duration must be between 4 and 32 beats")
    return True

def validate_composition_input(inputs: Dict[str, Any]) -> bool:
    """Validate all composition inputs"""
    required_fields = ['musician_input', 'style']
    for field in required_fields:
        if field not in inputs:
            raise InvalidInputError(f"Missing required field: {field}")
    
    validate_music_input(inputs['musician_input'])
    validate_style(inputs['style'])
    
    if 'key' in inputs:
        validate_key(inputs['key'])
    if 'instrument' in inputs:
        validate_instrument(inputs['instrument'])
    if 'tempo' in inputs:
        validate_tempo(inputs['tempo'])
    if 'duration' in inputs:
        validate_duration(inputs['duration'])
    
    return True
