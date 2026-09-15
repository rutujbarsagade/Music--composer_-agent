"""LangGraph workflow for music composition"""

import logging
from langgraph.graph import StateGraph, END

from src.state import MusicState
from src.components import (
    melody_generator,
    harmony_creator,
    rhythm_analyzer,
    style_adapter,
    midi_converter
)
from src.exceptions import MusicGenerationError

logger = logging.getLogger(__name__)

def create_workflow():
    """Create and compile the music composition workflow"""
    try:
        logger.info("Creating workflow...")
        
        # Initialize the StateGraph
        workflow = StateGraph(MusicState)
        
        # Add nodes to the graph
        workflow.add_node("melody_generator", melody_generator)
        workflow.add_node("harmony_creator", harmony_creator)
        workflow.add_node("rhythm_analyzer", rhythm_analyzer)
        workflow.add_node("style_adapter", style_adapter)
        workflow.add_node("midi_converter", midi_converter)
        
        # Set the entry point of the graph
        workflow.set_entry_point("melody_generator")
        
        # Add edges to connect the nodes
        workflow.add_edge("melody_generator", "harmony_creator")
        workflow.add_edge("harmony_creator", "rhythm_analyzer")
        workflow.add_edge("rhythm_analyzer", "style_adapter")
        workflow.add_edge("style_adapter", "midi_converter")
        workflow.add_edge("midi_converter", END)
        
        # Compile the graph
        app = workflow.compile()
        logger.info("Workflow created successfully")
        
        return app
    
    except Exception as e:
        logger.error(f"Error creating workflow: {e}")
        raise MusicGenerationError(f"Failed to create workflow: {str(e)}")
