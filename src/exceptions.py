"""Custom exceptions for the Music Compositor"""

class MusicCompositorException(Exception):
    """Base exception for Music Compositor"""
    pass

class MusicGenerationError(MusicCompositorException):
    """Raised when music generation fails"""
    pass

class MIDIConversionError(MusicCompositorException):
    """Raised when MIDI conversion fails"""
    pass

class AudioPlaybackError(MusicCompositorException):
    """Raised when audio playback fails"""
    pass

class ConfigurationError(MusicCompositorException):
    """Raised when configuration is invalid"""
    pass

class InvalidInputError(MusicCompositorException):
    """Raised when input validation fails"""
    pass
