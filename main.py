from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from summarizer import generate_summary, extract_action_items
from notion import push_tasks_to_notion

app = FastAPI(title="Meeting Scribe API")

# Enable CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store all meeting tasks cumulatively
all_tasks = []

# Request model
class TranscriptRequest(BaseModel):
    transcript: str


# Action item model
class ActionItem(BaseModel):
    owner: str
    task: str
    deadline: str
    status: str


# API response model
class AnalyzeResponse(BaseModel):
    summary: str
    action_items: List[ActionItem]


# Health check API
@app.get("/health")
def health_check():
    return {"status": "ok"}


# Main transcript analysis API
@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_transcript(request: TranscriptRequest):

    # Generate summary
    summary = generate_summary(request.transcript)

    # Extract tasks
    action_items = extract_action_items(request.transcript)

    # Store tasks cumulatively
    all_tasks.extend(action_items)

    # Push tasks to Notion database
    try:
        push_tasks_to_notion(action_items)
    except Exception as e:
        print("Notion Error:", e)

    # Return summary + ALL tasks
    return {
        "summary": summary,
        "action_items": all_tasks
    }