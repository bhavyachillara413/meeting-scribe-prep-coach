# Meeting Scribe & Prep Coach Backend

A simple FastAPI backend for analyzing meeting transcripts. It extracts a brief summary and identifies action items based on a simple rule-based NLP approach.

## Setup

1. Open your terminal in this directory.
2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

Run the application using Uvicorn:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.
You can access the interactive API documentation at `http://localhost:8000/docs`.

## Endpoints

### `GET /health`
Returns the health status of the API.

### `POST /analyze`
Analyzes a transcript and returns a summary and extracted action items.

**Input:**
```json
{
  "transcript": "Alice: We need to fix the login bug before Friday.\nBob: I will handle it by Thursday."
}
```

**Output:**
```json
{
  "summary": "Alice: We need to fix the login bug before Friday. Bob: I will handle it by Thursday.",
  "action_items": [
    {
      "owner": "Alice",
      "task": "We need to fix the login bug before Friday."
    },
    {
      "owner": "Bob",
      "task": "I will handle it by Thursday."
    }
  ]
}
```
# Meeting Scribe & Prep Coach

## Overview

Meeting Scribe & Prep Coach is an AI-powered productivity assistant that transforms meeting conversations into structured summaries, actionable tasks, deadlines, and productivity workflows.

The system automatically:

* Generates meeting summaries
* Detects speakers
* Extracts action items
* Identifies deadlines
* Stores tasks in Notion
* Displays cumulative meeting tasks in a frontend dashboard

---

# Problem Statement

In modern organizations, meetings generate large amounts of discussion, but important tasks and decisions are often lost.

Teams rely heavily on:

* manual note-taking
* scattered follow-ups
* unstructured documentation
* repeated discussions

This leads to:

* missed deadlines
* poor accountability
* duplicated work
* reduced productivity

Our project automates post-meeting productivity workflows by converting meeting conversations into actionable insights.

---

# Features

## Current Features

* Meeting summary generation
* Speaker-wise task extraction
* Deadline detection
* Status tracking
* Notion database integration
* Cumulative task dashboard
* React frontend interface
* FastAPI backend

---

# System Workflow

Meeting Conversation
↓
Frontend Input (React)
↓
FastAPI Backend
↓
Regex + NLP Processing
↓
Summary Generation
↓
Task & Deadline Extraction
↓
Notion Database Storage
↓
Frontend Productivity Dashboard

---

# Tech Stack

## Frontend

* React
* Vite
* CSS

## Backend

* FastAPI
* Python

## Processing

* Regex-based NLP heuristics
* Speaker detection
* Deadline extraction

## Database & Integration

* Notion API

---

# Project Structure

```
meeting-scribe-prep-coach/
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── App.jsx
│
├── main.py
├── summarizer.py
├── notion.py
├── requirements.txt
└── README.md
```

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone <your-github-repo>
cd meeting-scribe-prep-coach
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Frontend Dependencies

```bash
cd frontend
npm install
```

---

# Running the Project

## Start Backend

From project root:

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## Start Frontend

Open another terminal:

```bash
cd frontend
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# API Endpoint

## POST /analyze

### Request

```json
{
  "transcript": "Rahul: Complete API integration tonight."
}
```

---

### Response

```json
{
  "summary": "The team discussed API integration.",
  "action_items": [
    {
      "owner": "Rahul",
      "task": "Complete API integration",
      "deadline": "tonight",
      "status": "To Do"
    }
  ]
}
```

---

# Example Meetings

## Meeting 1

```text
Sarah: Finalize login feature before Friday.
David: Complete backend authentication changes by Thursday evening.
Emily: Test UI responsiveness tomorrow.
```

## Meeting 2

```text
Alex: Deploy payment module before release.
Sophia: Complete deployment testing by Friday.
Daniel: Review API security tomorrow.
```

---

# Notion Integration

Tasks are automatically stored in a Notion database.

Required environment variables:

```env
NOTION_TOKEN=your_notion_token
NOTION_DATABASE_ID=your_database_id
```

Stored fields:

* Task
* Owner
* Deadline
* Status

---

# AI Usage Disclosure

This project uses AI-assisted development tools for:

* architecture planning
* frontend generation assistance
* backend development support
* presentation preparation
* debugging guidance

No external LLM APIs are currently used for transcript processing.
Current NLP logic uses regex-based heuristics implemented locally in Python.

---

# Future Enhancements

Planned upgrades:

* Whisper speech-to-text integration
* Claude/OpenAI summarization
* Jira integration
* RAG-based meeting memory
* Calendar synchronization
* AI-powered meeting preparation assistant

---

# Impact

Meeting Scribe & Prep Coach helps teams:

* reduce manual effort
* improve accountability
* automate follow-up workflows
* centralize meeting intelligence
* improve productivity tracking

---

# Team

MSRIT_Hawkers

Members:

* Bhavya Chillara
* Batthula Bhavya Sree
* Jalimanchi Sree Kruthi
* Manasa Rajendran


## Demo Video

https://drive.google.com/file/d/1t6SG4coEMNqDxFK_GZMWYh8oE4_N4Bth/view?usp=sharing
