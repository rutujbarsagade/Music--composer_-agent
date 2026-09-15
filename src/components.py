"""Component functions for music composition workflow"""

from typing import Dict
import logging
import random
import tempfile
import music21
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from src.state import MusicState
from src.config import config
from src.exceptions import MusicGenerationError, MIDIConversionError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize LLM
try:
    llm = ChatOpenAI(model=config.MODEL_NAME, temperature=config.TEMPERATURE)
    logger.info(f"LLM initialized with model: {config.MODEL_NAME}")
except Exception as e:
    logger.error(f"Failed to initialize LLM: {e}")
    raise

def melody_generator(state: MusicState) -> Dict:
    """Generate a melody based on the user's input."""
    try:
        logger.info("Generating melody...")
        prompt = ChatPromptTemplate.from_template(
            "Generate a melody based on this input: {input}. "
            "Represent it as a string of notes in music21 format. "
            "Keep it concise (50-100 words)."
        )
        chain = prompt | llm
        melody = chain.invoke({"input": state["musician_input"]})
        logger.info("Melody generated successfully")
        return {"melody": melody.content}
    except Exception as e:
        logger.error(f"Error generating melody: {e}")
        raise MusicGenerationError(f"Failed to generate melody: {str(e)}")

def harmony_creator(state: MusicState) -> Dict:
    """Create harmony for the generated melody."""
    try:
        logger.info("Creating harmony...")
        prompt = ChatPromptTemplate.from_template(
            "Create harmony for this melody: {melody}. "
            "Represent it as a string of chords in music21 format. "
            "Keep it concise (50-100 words)."
        )
        chain = prompt | llm
        harmony = chain.invoke({"melody": state["melody"]})
        logger.info("Harmony created successfully")
        return {"harmony": harmony.content}
    except Exception as e:
        logger.error(f"Error creating harmony: {e}")
        raise MusicGenerationError(f"Failed to create harmony: {str(e)}")

def rhythm_analyzer(state: MusicState) -> Dict:
    """Analyze and suggest a rhythm for the melody and harmony."""
    try:
        logger.info("Analyzing rhythm...")
        prompt = ChatPromptTemplate.from_template(
            "Analyze and suggest a rhythm for this melody and harmony: "
            "Melody: {melody}, Harmony: {harmony}. "
            "Represent it as a string of durations in music21 format. "
            "Keep it concise (50-100 words)."
        )
        chain = prompt | llm
        rhythm = chain.invoke({
            "melody": state["melody"],
            "harmony": state["harmony"]
        })
        logger.info("Rhythm analyzed successfully")
        return {"rhythm": rhythm.content}
    except Exception as e:
        logger.error(f"Error analyzing rhythm: {e}")
        raise MusicGenerationError(f"Failed to analyze rhythm: {str(e)}")

def style_adapter(state: MusicState) -> Dict:
    """Adapt the composition to the specified musical style."""
    try:
        logger.info(f"Adapting to style: {state['style']}")
        prompt = ChatPromptTemplate.from_template(
            "Adapt this composition to the {style} style. "
            "Melody: {melody}, Harmony: {harmony}, Rhythm: {rhythm}. "
            "Provide the result in music21 format. "
            "Keep it concise (50-100 words)."
        )
        chain = prompt | llm
        adapted = chain.invoke({
            "style": state["style"],
            "melody": state["melody"],
            "harmony": state["harmony"],
            "rhythm": state["rhythm"]
        })
        logger.info(f"Style adapted to {state['style']} successfully")
        return {"composition": adapted.content}
    except Exception as e:
        logger.error(f"Error adapting style: {e}")
        raise MusicGenerationError(f"Failed to adapt style: {str(e)}")

def midi_converter(state: MusicState) -> Dict:
    """Convert the composition to MIDI format and save it as a file."""
    try:
        logger.info("Converting to MIDI...")
        
        # Create a new score
        piece = music21.stream.Score()
        
        # Parse the user input to determine scale
        user_input = state['musician_input'].lower()
        scale_name = 'C major'
        
        if 'minor' in user_input:
            scale_name = 'C minor'
        elif 'major' in user_input:
            scale_name = 'C major'
        else:
            scale_name = random.choice(list(config.SCALES.keys()))
        
        logger.info(f"Using scale: {scale_name}")
        
        # Create melody
        melody = music21.stream.Part()
        scale = config.SCALES[scale_name]
        
        duration = state.get('duration', config.DEFAULT_DURATION)
        for _ in range(duration):
            try:
                note = music21.note.Note(random.choice(scale) + '4')
                note.quarterLength = 1
                melody.append(note)
            except Exception as e:
                logger.warning(f"Error creating note: {e}")
                continue
        
        # Create harmony
        harmony = music21.stream.Part()
        for _ in range(duration):
            try:
                chord_name = random.choice(list(config.CHORDS.keys()))
                chord = music21.chord.Chord(config.CHORDS[chord_name])
                chord.quarterLength = 1
                harmony.append(chord)
            except Exception as e:
                logger.warning(f"Error creating chord: {e}")
                continue
        
        # Add parts to score
        piece.append(melody)
        piece.append(harmony)
        
        # Set tempo
        tempo = state.get('tempo', config.DEFAULT_TEMPO)
        piece.insert(0, music21.tempo.MetronomeMark(number=tempo))
        
        logger.info(f"Using tempo: {tempo} BPM")
        
        # Save to temporary MIDI file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mid') as temp_midi:
            try:
                piece.write('midi', temp_midi.name)
                logger.info(f"MIDI file created: {temp_midi.name}")
            except Exception as e:
                logger.error(f"Error writing MIDI file: {e}")
                raise MIDIConversionError(f"Failed to write MIDI file: {str(e)}")
        
        return {"midi_file": temp_midi.name}
    
    except MIDIConversionError:
        raise
    except Exception as e:
        logger.error(f"Error in MIDI conversion: {e}")
        raise MIDIConversionError(f"Failed to convert to MIDI: {str(e)}")
