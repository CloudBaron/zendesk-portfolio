# Project 3 — Zendesk API: Auto-Ticket Creator & Reporter

**Difficulty:** Advanced  
**Time to complete:** 3–5 hours  
**Platform:** Zendesk REST API + Python

---

## Overview

This project uses the Zendesk REST API to automate two common support operations:
1. **Create tickets programmatically** — simulating how a product or integration might auto-generate support tickets
2. **Pull and report on ticket data** — generating a CSV summary of ticket volume by status for the last 7 days

This is the kind of work done by Integration Engineers and CX Operations teams to connect Zendesk with other tools and extract actionable data.

---

## Features

- `create_ticket.py` — POSTs a new ticket to Zendesk via the API with custom fields
- `report.py` — GETs all tickets from the past 7 days and writes a summary CSV
- Credentials stored securely in a `.env` file (never committed to GitHub)
- Clean, commented code with error handling

---

## Project Structure

```
project-3-api/
├── README.md
├── .env.example          ← Template for credentials (safe to commit)
├── create_ticket.py      ← Script to create a ticket via API
├── report.py             ← Script to pull tickets and generate CSV report
├── sample_report.csv     ← Example output from report.py
└── screenshots/
    └── (your screenshots here)
```

---

## Setup Instructions

### 1. Clone this repo
```bash
git clone https://github.com/YOUR_USERNAME/zendesk-portfolio.git
cd zendesk-portfolio/project-3-api
```

### 2. Install dependencies
```bash
pip install requests python-dotenv
```

### 3. Set up your credentials
Copy `.env.example` to `.env` and fill in your values:
```bash
cp .env.example .env
```

Open `.env` and add:
```
ZENDESK_SUBDOMAIN=your-subdomain
ZENDESK_EMAIL=your-email@example.com
ZENDESK_API_TOKEN=your_api_token_here
```

**To get your API token in Zendesk:**  
Admin Center → Apps & Integrations → APIs → Zendesk API → Enable Token Access → Add API Token

### 4. Run the scripts
```bash
# Create a test ticket
python create_ticket.py

# Generate a ticket report
python report.py
```

---

## Example Output

After running `report.py`, a `ticket_report.csv` file is generated:

```
status,count
new,4
open,12
pending,3
solved,27
closed,8
```

See `sample_report.csv` for a full example.

---

## Screenshots

> Add screenshots of your terminal output and Zendesk ticket view after running the scripts.

```
![create_ticket.py running](./screenshots/create-ticket-output.png)
![Ticket created in Zendesk](./screenshots/ticket-in-zendesk.png)
![report.py CSV output](./screenshots/report-output.png)
```

---

## Skills Demonstrated

- Zendesk REST API authentication (API token)
- HTTP POST and GET requests with Python (`requests` library)
- Environment variable management with `.env` / `python-dotenv`
- Data extraction and CSV reporting
- Error handling and clean code practices
- Integration Engineering fundamentals
