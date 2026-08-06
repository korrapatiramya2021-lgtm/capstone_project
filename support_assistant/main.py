from fastapi import FastAPI
from pydantic import BaseModel
from graph import app_graph

app = FastAPI(title="Zepto Support Assistant")

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    sources: list[str]
    confidence: float

@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):

    result = app_graph.invoke({
        "question": request.question,
        "intent": "",
        "answer": ""
    })

    return AnswerResponse(
        answer=result["answer"],
        sources=["doc_01"],
        confidence=0.95
    )
