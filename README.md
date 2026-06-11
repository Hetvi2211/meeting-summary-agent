# Meeting Summary Agent

## Overview

Meeting Summary Agent is a custom AI agent built using Python and Google Gemini API.

The agent reads a meeting transcript, analyzes the discussion, extracts important information, and generates:

* Meeting Summary
* Action Items
* Owners/Assignees

The generated summary is saved to a text file and stored in a SQLite database for future reference.

---

## Features

* Transcript Analysis using Gemini
* Meeting Summary Generation
* Action Item Extraction
* Owner Identification
* Save Summary to Text File
* Save Summary to SQLite Database
* Custom Agent Implementation (No Workflow Tools)

---

## Project Structure

meeting-summary-agent/

├── app.py

├── database.py

├── view_db.py

├── meeting_summaries.db

├── outputs/

│ └── meeting_summary.txt

└── transcripts/

└── sample_meeting.txt

---

## Tools Used

### Tool 1: Transcript Reader

Reads meeting transcripts from text files.

### Tool 2: Summary Storage

Stores generated summaries in:

* Text File
* SQLite Database

---

## Technologies

* Python
* Google Gemini API
* SQLite
* python-dotenv

---

## Sample Output

### Meeting Summary

The meeting focused on the upcoming dashboard launch scheduled for next week. Backend API development is complete. Frontend testing remains pending and must be completed by Friday. Documentation preparation is required. Deployment responsibilities were assigned.

### Action Items

* Complete frontend testing
* Prepare documentation
* Deploy application

### Owners

* Hetvi → Frontend Testing
* Nauman → Deployment
* Team → Documentation

---

## Screenshots

### Meeting agent

![Meeting agent](screenshots/meeting-agent-demo.png)

### Saved output

![Saved output](screenshots/saved-output.png)

### Database Records

![Database](screenshots/db-meeting-summaries.png)

### Live Demo

![live demo](screenshots/live-deploy1.png)

### Meeting Summary

![live demo](screenshots/metting-summary-output.png)

### Github Actions Success

![Github Actions Success](screenshots/github-actions-success.png)

---

## Live Demo

Production URL:

https://ask-my-notes-qkef.vercel.app/

---

## Deployment

Platform: Vercel

SSL: Enabled Automatically

Status: Live

---

## CI/CD Pipeline

GitHub Actions automatically:

- Installs dependencies
- Verifies Flask app syntax
- Runs on every push
- Runs on Pull Requests

Workflow File:

.github/workflows/ci.yml

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Create .env file:

GEMINI_API_KEY=your_api_key

Run agent:

python app.py

View database records:

python view_db.py

---

## What I Would Do With More Time

- Add user authentication
- Store summaries in database
- Export summaries as PDF
- Add file upload support
- Add meeting analytics dashboard
- Improve prompt engineering

---

## Learning Outcomes

* Built a custom AI agent without workflow automation tools.
* Integrated Google Gemini API.
* Implemented tool usage within an agent workflow.
* Generated structured meeting summaries.
* Stored outputs in files and databases.
* Understood real-world AI agent architecture.


