# CC LAB 2 – Monolithic Architecture

A simple **monolithic event registration web application** built with **FastAPI**, **Jinja2**, and **SQLite**.

This project demonstrates a single-service architecture where user authentication, event browsing, event registration, and checkout logic all live in one codebase.

## Project Summary

This app simulates a college fest registration portal where users can:
- Create an account and log in
- Browse available events
- Register for events
- View their registered events
- See a computed checkout total

The application is intentionally monolithic and includes a few performance and reliability anti-patterns that are useful for lab exercises (e.g., debugging, profiling, load testing with Locust, and error handling walkthroughs).

## Features

- User registration and login
- Event listing from SQLite database
- Event registration flow
- "My Events" page for user-specific registrations
- Checkout page with total fee calculation
- Global exception handler with a custom error page
- Locust load-testing scripts for key routes

## How to Install

### 1) Clone the repository

```bash
git clone https://github.com/Srikar62/CC-LAB-2---MONOLITHIC-ARCHITECTURE-
cd REPO
```

### 2) (Optional but recommended) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows PowerShell
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Seed the events table

```bash
python insert_events.py
```

## How to Run

Start the FastAPI server with Uvicorn:

```bash
uvicorn main:app --reload
```

Then open your browser at:

- App URL: `http://127.0.0.1:8000`
- Suggested first page: `http://127.0.0.1:8000/register`

## Example Usage

1. Open `/register` and create a user account.
2. Log in from `/login`.
3. Browse events on `/events?user=<username>`.
4. Register for an event from the list.
5. View enrolled events at `/my-events?user=<username>`.
6. Open `/checkout` to see the total registration fee.

## Future Ideas

- Add password hashing and session/token-based authentication
- Replace query-string user identity with secure auth middleware
- Improve database schema with foreign keys and constraints
- Add unit/integration tests with `pytest`
- Containerize with Docker and add CI checks
- Refactor monolith into services (auth, events, checkout)
- Add observability (structured logs, metrics, tracing)
- Improve UI/UX and add API docs for all flows

---

If you are using this for a class lab, you can extend this project to compare monolithic and microservices architectures under load.
