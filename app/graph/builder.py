# Graph builder 
from langgraph.graph import StateGraph
from app.graph.state import AgentState
from app.graph.nodes.intent_node import intent_node

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("intent_router", intent_node)

    builder.set_entry_point("intent_router")

    builder.set_finish_point("intent_router")

    return builder.compile()