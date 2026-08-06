from typing import TypedDict
from langgraph.graph import StateGraph, END
from prompts import PROMPT_TEMPLATE

# Graph State
class GraphState(TypedDict):
    question: str
    intent: str
    answer: str

# Intent Classification
def classify_intent(state):
    question = state["question"].lower()

    keywords = [
        "delivery", "refund", "return", "membership",
        "tracking", "cancel", "gift", "support", "damaged"
    ]

    if any(word in question for word in keywords):
        state["intent"] = "policy"
    else:
        state["intent"] = "general"

    return state

# Retrieve and Answer (Mock Mode)
def retrieve_and_answer(state):
    state["answer"] = "Based on the retrieved context: Orders below INR 149 incur a flat INR 25 delivery fee. Standard delivery is free on orders above INR 149."
    return state

# Direct Answer
def direct_answer(state):
    state["answer"] = "This question does not require document retrieval."
    return state

# Routing
def route(state):
    if state["intent"] == "policy":
        return "retrieve_and_answer"
    return "direct_answer"

# Build Graph
workflow = StateGraph(GraphState)

workflow.add_node("classify_intent", classify_intent)
workflow.add_node("retrieve_and_answer", retrieve_and_answer)
workflow.add_node("direct_answer", direct_answer)

workflow.set_entry_point("classify_intent")

workflow.add_conditional_edges(
    "classify_intent",
    route,
    {
        "retrieve_and_answer": "retrieve_and_answer",
        "direct_answer": "direct_answer",
    },
)

workflow.add_edge("retrieve_and_answer", END)
workflow.add_edge("direct_answer", END)

app_graph = workflow.compile()
