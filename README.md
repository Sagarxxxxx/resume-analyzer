# ResumeIQ 🎯
### AI-Powered Resume Analyzer built with Google Gemini + FastAPI + React

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=flat&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=flat&logo=react&logoColor=black)
![Gemini](https://img.shields.io/badge/Google_Gemini-API-4285F4?style=flat&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

> Built for **HackFest 2026** — AI & Smart Automation Track

---

## 📸 Screenshots

> _Add your screenshots here after running the app_

| Upload Screen | Results Screen |
|---|---|
| ![Upload](https://placehold.co/500x300?text=Upload+Screen) | ![Results](https://placehold.co/500x300?text=Results+Screen) |

---

## ✨ Features

- 📊 **ATS Score** — See how well your resume passes Applicant Tracking Systems
- 🧠 **Candidate Summary** — AI-generated 2-3 sentence profile of your resume
- ✅ **Top Strengths** — What you're already doing right
- ⚠️ **Critical Missing Skills** — What's holding your resume back
- 📝 **Formatting Feedback** — Layout, readability, and typo analysis
- 🔁 **XYZ Bullet Rewrites** — Weak bullets rewritten using Google's hiring framework, with reasoning

---

## 🏗️ Tech Stack

| Layer | Tech |
|---|---|
| Frontend | React 18 (zero build step — single HTML file) |
| Backend | Python 3.10+ + FastAPI |
| AI | Google Gemini 1.5 Flash |
| PDF Parsing | pdfplumber |
| Env Management | python-dotenv |

---

## 📁 Project Structure

```
resumeiq/
├── backend/
│   ├── main.py           # FastAPI app + Gemini integration
│   ├── requirements.txt  # Python dependencies
│   ├── .env              # Your API key goes here (never committed)
│   └── .gitignore
├── frontend/
│   └── index.html        # React frontend (no npm needed)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A Google Gemini API key → [Get one free here](https://aistudio.google.com/app/apikey)

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/resumeiq.git
cd resumeiq
```

### 2. Set up the backend
```bash
cd backend
pip install -r requirements.txt
```

### 3. Add your Gemini API key
Create a `.env` file inside the `backend/` folder:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the backend
```bash
uvicorn main:app --reload
# API runs at http://localhost:8000
```

### 5. Open the frontend
```bash
cd ../frontend
# Just open index.html in your browser — no npm, no build step!
```

---

## 🔌 API Reference

### `POST /analyze`

Analyzes a resume PDF and returns structured AI feedback.

**Request:** `multipart/form-data`

| Field | Type | Description |
|---|---|---|
| `resume` | File | PDF resume file |

**Response:**
```json
{
  "filename": "my_resume.pdf",
  "status": "success",
  "analysis": {
    "overall_ats_score": 72,
    "brief_summary": "...",
    "top_strengths": ["...", "..."],
    "critical_missing_skills": ["...", "..."],
    "resume_formatting_feedback": "...",
    "bullet_point_improvements": [
      {
        "original_text": "Worked on backend APIs",
        "improved_text": "Engineered 15+ RESTful APIs using FastAPI, reducing latency by 30%.",
        "reasoning": "Adds scope, technology, and measurable impact."
      }
    ]
  }
}
```

---

## 💡 How the AI Works

The core intelligence is a single, carefully engineered prompt sent to **Gemini 1.5 Flash**. It instructs the model to act as an elite ATS and technical recruiter, then return a **strictly typed JSON object** using:

```python
generation_config=genai.types.GenerationConfig(
    response_mime_type="application/json"
)
```

This guarantees clean, parseable JSON every time — no markdown stripping needed.

The **XYZ rewrite format** (Accomplished **X**, measured by **Y**, by doing **Z**) is the same framework used by Google's hiring team to evaluate candidate impact.

---

## 🗺️ Roadmap

- [ ] Job description input for targeted keyword matching
- [ ] Role selector (SWE / Data Science / Product Manager)
- [ ] Side-by-side resume diff view
- [ ] Export improved resume as PDF
- [ ] User accounts + resume history

---

## 📝 Dev.to Post

Read the full write-up on how I built this:
👉 [**I Built an AI Resume Analyzer in 24 Hours Using Gemini API**](https://dev.to/YOUR_USERNAME/your-post-slug)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

MIT License — feel free to use this for your own projects.

---

<p align="center">Built with ❤️ for HackFest 2026 by <a href="https://github.com/YOUR_USERNAME">YOUR_NAME</a></p>
