# 🎵 AI Music Compositor using LangGraph

## Overview

An advanced AI-powered music composition system that generates unique musical compositions using LangGraph workflows and OpenAI's language models. The system creates melodies, harmonies, and rhythms, adapting them to specified musical styles, and outputs playable MIDI files.

## Features

✨ **Core Features**
- 🎼 AI-powered melody generation
- 🎵 Automatic harmony creation
- ⏱️ Rhythm analysis and adaptation
- 🎨 Musical style adaptation (15+ styles)
- 🎹 Support for multiple instruments
- 📊 Customizable musical keys and tempos
- 🔊 MIDI file generation and playback
- 🎛️ Interactive Jupyter notebook UI

🛡️ **Reliability & Optimization**
- Comprehensive error handling
- Input validation
- Logging throughout the application
- Optimized LLM prompts
- Resource cleanup

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API Key

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/rutujbarsagade/Music--composer_-agent.git
cd Music--composer_-agent
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Usage

### Jupyter Notebook (Recommended)

```bash
jupyter notebook music_compositor_interactive.ipynb
```

The notebook provides an interactive UI with:
- Music description input
- Style selection (15 genres)
- Key and instrument selection
- Tempo and duration controls
- Generate, Play, and Reset buttons

### Python Script

```python
from src.config import config
from src.workflow import create_workflow
from src.validators import validate_composition_input
from src.audio import AudioPlayer

# Validate configuration
config.validate()

# Create workflow
app = create_workflow()

# Prepare input
inputs = {
    "musician_input": "Create a happy piano piece in C major",
    "style": "Romantic era",
    "key": "C major",
    "instrument": "Piano",
    "tempo": 60,
    "duration": 8
}

# Validate input
validate_composition_input(inputs)

# Generate composition
result = app.invoke(inputs)

# Play the result
player = AudioPlayer()
player.play(result['midi_file'])
player.cleanup()
```

## Project Structure

```
Music--composer_-agent/
├── src/
│   ├── __init__.py              # Package initialization
│   ├── config.py                # Configuration management
│   ├── state.py                 # State definitions
│   ├── exceptions.py            # Custom exceptions
│   ├── validators.py            # Input validators
│   ├── components.py            # Workflow components
│   ├── workflow.py              # Main workflow
│   └── audio.py                 # Audio playback
├── notebooks/
│   └── music_compositor_interactive.ipynb  # Interactive UI
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
├── README.md                    # This file
└── LICENSE                      # License
```

## Configuration

Edit `.env` file to customize:

```bash
# OpenAI API
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini
TEMPERATURE=0.7
MAX_TOKENS=2000

# Audio
AUDIO_FORMAT=wav
SAMPLE_RATE=44100
```

## Supported Styles

Classical, Romantic era, Jazz, Blues, Rock, Pop, Electronic, Ambient, Folk, Heavy Metal, Hip Hop, Country, R&B, Reggae, Latin

## Supported Instruments

Piano, Guitar, Violin, Flute, Trumpet, Cello, Drums, Synthesizer, Harp, Organ

## Supported Keys

C major, C minor, C# major, D major, D minor, Eb major, E major, E minor, F major, F# major, G major, G minor, Ab major, A major, A minor, Bb major, B major, B minor

## Error Handling

The system includes comprehensive error handling:

- **MusicGenerationError**: Raised when music generation fails
- **MIDIConversionError**: Raised when MIDI conversion fails
- **AudioPlaybackError**: Raised when audio playback fails
- **ConfigurationError**: Raised when configuration is invalid
- **InvalidInputError**: Raised when input validation fails

## Logging

The application logs all operations to help with debugging:

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

## Performance Tips

1. **API Rate Limiting**: The system respects OpenAI API rate limits
2. **Token Optimization**: Prompts are optimized to reduce token usage
3. **Caching**: Consider implementing result caching for repeated compositions
4. **Batch Processing**: Process multiple compositions sequentially

## Troubleshooting

### "OPENAI_API_KEY is not set"
- Ensure `.env` file exists and contains your API key
- Run `cp .env.example .env` and edit the file

### "Failed to initialize audio player"
- Ensure pygame is installed: `pip install pygame`
- On Linux, you may need additional system packages

### "Invalid input" errors
- Check that inputs match the expected formats
- Refer to supported styles, instruments, and keys
- Ensure text inputs are between required character limits

## Optimization Features

✅ **Code Optimization**
- Type hints for better IDE support
- Modular design for easy maintenance
- Separation of concerns
- DRY principle throughout

✅ **Error Handling**
- Try-catch blocks with specific exception types
- Graceful error recovery
- Informative error messages
- Logging for debugging

✅ **Performance**
- Optimized LLM prompts (50-100 words)
- Efficient resource management
- Connection pooling
- Async support ready

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Author

Created by **Rutuj Barsagade**

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing documentation
- Review error logs

## Roadmap

- [ ] Async workflow support
- [ ] Web UI with Flask/FastAPI
- [ ] Advanced MIDI editing
- [ ] Music theory analysis
- [ ] Real-time collaboration
- [ ] Cloud deployment guides
- [ ] Mobile app support
- [ ] Multiple language models support

## Acknowledgments

- LangGraph for workflow orchestration
- LangChain for LLM integration
- OpenAI for GPT models
- music21 for MIDI manipulation
- pygame for audio playback
