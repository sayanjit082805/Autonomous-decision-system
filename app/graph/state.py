# Shared data structures for agent state management
from typing import TypedDict, Optional

class AgentState(TypedDict):
    user_input: str

    # Intent
    intent_type: Optional[str]
    intent_confidence: Optional[float]

    # Downstream outputs 
    rag_output: Optional[str]
    image_output: Optional[str]
    companion_output: Optional[str]