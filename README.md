# Smart Knowledge Assistant

This is an AI-powered project that can analyze website content, generate summaries, and answer user questions based on the website information.

The project was developed using FastAPI, HTML/CSS/JavaScript, LangChain, FAISS, and Groq API.

---

## Features

- Website content analysis
- AI-generated website summary
- Question answering system
- Semantic search using vector embeddings
- FastAPI backend
- Interactive frontend

---

## How It Works

1. User enters a website URL
2. The system extracts website content
3. Content is split into smaller chunks
4. Chunks are converted into embeddings
5. FAISS stores the vector data
6. AI generates summaries and answers

---

## Technologies Used

- Python
- FastAPI
- HTML/CSS/JavaScript
- LangChain
- FAISS
- HuggingFace Embeddings
- Groq API

---

## Screenshots

### Homepage
![Homepage](screenshots/home.png)

### Website Summary
![Summary](screenshots/summary.png)

### Question Answering
![Q&A](screenshots/qa.png)

---

## How to Run

### Install Requirements

```bash
pip install -r requirements.txt
```

### Create .env File

```env
GROQ_API_KEY=your_api_key
```

### Run Backend

```bash
uvicorn api:app --reload
```

### Run Frontend

```bash
cd frontend
python -m http.server 8001
```

Open:
```text
http://localhost:8001
```

---

## Future Improvements

- OCR support
- PDF upload support
- Better UI design
- Database integration

---

## Developed By

Tilak Naik