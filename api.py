from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # ✅ ADD THIS
from pydantic import BaseModel

from services.web_loader import load_website
from services.text_processing import split_text
from services.vector_store import create_vector_store
from services.qa_engine import answer_question, summarize_website

app = FastAPI()

# ✅ ADD THIS BLOCK (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow frontend
    allow_credentials=True,
    allow_methods=["*"],      # allow POST, OPTIONS
    allow_headers=["*"],
)

vector_db = None


class URLRequest(BaseModel):
    url: str


class QuestionRequest(BaseModel):
    question: str


@app.post("/analyze")
def analyze(data: URLRequest):
    global vector_db

    docs = load_website(data.url)
    chunks = split_text(docs)
    vector_db = create_vector_store(chunks)

    summary = summarize_website(vector_db)

    return {"summary": summary}


@app.post("/ask")
def ask(data: QuestionRequest):
    global vector_db

    answer = answer_question(vector_db, data.question)

    return {"answer": answer}