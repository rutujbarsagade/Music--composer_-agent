"""Audio playback functionality"""

import logging
import pygame
from pathlib import Path

from src.exceptions import AudioPlaybackError

logger = logging.getLogger(__name__)

class AudioPlayer:
    """Handles MIDI file playback"""
    
    def __init__(self):
        """Initialize the audio player"""
        try:
            pygame.mixer.init()
            logger.info("Audio player initialized")
        except Exception as e:
            logger.error(f"Failed to initialize audio player: {e}")
            raise AudioPlaybackError(f"Failed to initialize audio player: {str(e)}")
    
    def play(self, midi_file_path: str) -> bool:
        """Play a MIDI file"""
        try:
            if not Path(midi_file_path).exists():
                raise FileNotFoundError(f"MIDI file not found: {midi_file_path}")
            
            logger.info(f"Playing: {midi_file_path}")
            pygame.mixer.music.load(midi_file_path)
            pygame.mixer.music.play()
            
            # Wait for playback to finish
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            logger.info("Playback finished")
            return True
        
        except FileNotFoundError as e:
            logger.error(f"File not found: {e}")
            raise AudioPlaybackError(str(e))
        except Exception as e:
            logger.error(f"Error during playback: {e}")
            raise AudioPlaybackError(f"Failed to play audio: {str(e)}")
    
    def stop(self) -> bool:
        """Stop audio playback"""
        try:
            pygame.mixer.music.stop()
            logger.info("Playback stopped")
            return True
        except Exception as e:
            logger.error(f"Error stopping playback: {e}")
            return False
    
    def cleanup(self) -> bool:
        """Clean up audio resources"""
        try:
            pygame.mixer.quit()
            logger.info("Audio player cleaned up")
            return True
        except Exception as e:
            logger.error(f"Error cleaning up audio: {e}")
            return False
