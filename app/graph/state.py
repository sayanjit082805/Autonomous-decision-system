# Shared data structures for agent state management
from typing import TypedDict, Optional

class AgentState(TypedDict):
    user_input: str
    intent_type: Optional[str]
    intent_confidence: Optional[float]