
# Gemini Chatbot 🤖

[![Python](https://img.shields.io/badge/Python-3.12+-blue)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18+-blue)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-blue)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A modern AI chatbot web application using **FastAPI** for the backend and **React** for the frontend, integrated with **Google Gemini API** for natural language responses.

---

## Features
- Clean and responsive chat interface.
- Smooth scrolling messages with typing indicator.
- Supports Google Gemini API for AI-powered responses.
- Gradient theme using **orange and blue colors**.
- Handles API errors gracefully.

---

## Project Structure

```
gemini-chatbot/
├── backend/
│   ├── main.py          # FastAPI server
│   ├── list_models.py   # Script to list available Gemini models
│   └── .env             # Store GEMINI_API_KEY here (ignored by git)
├── frontend/
│   ├── src/
│   │   └── components/
│   │       └── ChatUI.jsx
│   └── package.json
├── .gitignore
└── README.md
```

---

## Backend Setup (FastAPI)

1. Create a virtual environment:
```bash
python -m venv myvenv
source myvenv/bin/activate  # macOS/Linux
myvenv\Scripts\activate     # Windows
```

2. Install backend dependencies:
```bash
pip install -r backend/requirements.txt
```

3. Create a `.env` file inside `backend/`:
```
GEMINI_API_KEY=your_api_key_here
```

4. Run the FastAPI server:
```bash
cd backend
uvicorn main:app --reload
```

- Access API at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- API docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Frontend Setup (React)

1. Navigate to frontend:
```bash
cd frontend
```

2. Install frontend dependencies:
```bash
npm install
# or
yarn
```

3. Start the React development server:
```bash
npm start
# or
yarn start
```

- App runs at [http://localhost:3000](http://localhost:3000)

---

## Usage

- Type a message in the input box.
- Press **Send** or hit **Enter**.
- The AI bot will respond using Gemini API.
- Messages auto-scroll for convenience.
- Free-tier quota may cause `RESOURCE_EXHAUSTED` errors.

---

## Notes

- Keep `.env` **private** — do not push API keys to GitHub.
- Use `list_models.py` to see available Gemini models.
- Free-tier has **daily request limits**.

---

