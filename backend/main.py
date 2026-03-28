from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai
import pdfplumber
import json
import os
import io

load_dotenv()  # Loads GEMINI_API_KEY from .env file

app = FastAPI(title="Resume Analyzer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Gemini API key from environment at startup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set. Add it to your .env file.")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def extract_text_from_pdf(file_bytes: bytes) -> str:
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

@app.post("/analyze")
async def analyze_resume(resume: UploadFile = File(...)):
    # 1. Validate file type
    if not resume.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    # 2. Read and extract text
    file_bytes = await resume.read()
    resume_text = extract_text_from_pdf(file_bytes)

    if not resume_text or len(resume_text) < 100:
        raise HTTPException(status_code=400, detail="Could not extract enough text from the PDF. Ensure it's not a scanned image.")

    # 3. Create the advanced JSON prompt
    prompt = f"""
    You are an elite Technical Recruiter and Applicant Tracking System (ATS) specializing in software engineering and tech roles.
    Your task is to analyze the provided resume text and return a strictly formatted JSON object.

    Evaluate the resume based on impact, clarity, action verbs, and quantifiable metrics.
    You must output the data in this exact JSON structure:
    {{
      "overall_ats_score": <int 0-100>,
      "brief_summary": "<string: 2-3 sentences summarizing the candidate's profile>",
      "top_strengths": ["<string>", "<string>"],
      "critical_missing_skills": ["<string>", "<string>"],
      "resume_formatting_feedback": "<string: feedback on text layout, typos, or readability>",
      "bullet_point_improvements": [
        {{
          "original_text": "<string: extract a weak, vague, or metric-less bullet point from the text>",
          "improved_text": "<string: rewrite it using the XYZ format (Accomplished X, measured by Y, by doing Z)>",
          "reasoning": "<string: why this rewrite is better>"
        }}
      ]
    }}
    Example of a good bullet rewrite:
    Original: "Solved coding problems."
    Improved: "Solved 200+ Data Structures and Algorithms problems in C++ to optimize execution time and memory allocation."

    Resume Text to Analyze:
    {resume_text}
    """

    try:
        # 4. Call Gemini, enforcing JSON output
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                response_mime_type="application/json",
            )
        )

        # 5. Return the structured AI analysis
        return {
            "filename": resume.filename,
            "status": "success",
            "analysis": json.loads(response.text)
        }

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Gemini returned an unexpected format. Please try again.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini API error: {str(e)}")

@app.get("/")
def root():
    return {"message": "Resume Analyzer API is running. POST to /analyze"}
