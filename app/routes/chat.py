from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.retriever import retrieve_context
from app.services.llm import ask_llm

router = APIRouter(prefix="/api", tags=["Chat"])

@router.post("/ask", response_model=ChatResponse)
def ask_college_ai(request: ChatRequest):
    context = retrieve_context(request.question)

    if not context:
        return {
            "answer": "Please contact the college office for this information."
        }

    answer = ask_llm(context, request.question)
    return {"answer": answer}