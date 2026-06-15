from fastapi import FastAPI,UploadFile, File, Form
from services.pdf_service import  extract_text
from services.embedding_service import generate_embedding
from services.similarity_service import calculate_similarity
from services.resume_filter import  Resume
from fastapi.middleware.cors import CORSMiddleware 
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import tempfile
import logging
import os

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


resume = Resume()


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR,exist_ok=True)
logger = logging.getLogger(__name__)

@app.post("/resume-match")
async def resume_match(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    temp_path = None

    try:
        # Validate file
        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed."
            )

        # Validate job description
        if not job_description.strip():
            raise HTTPException(
                status_code=400,
                detail="Job description cannot be empty."
            )

        # Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp:
            temp.write(await file.read())
            temp_path = temp.name

        # Extract resume text
        resume_text = extract_text(temp_path)

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="No readable text found in the uploaded resume."
            )

        # Filter relevant sections
        filtered_resume = Resume.filter_relevant_sections(
            resume_text
        )

        # Generate embeddings
        resume_embedding = generate_embedding(
            filtered_resume
        )

        jd_embedding = generate_embedding(
            job_description
        )

        # Calculate similarity score
        score = calculate_similarity(
            resume_embedding,
            jd_embedding
        )

        return {
            "filename": file.filename,
            "match_score": round(score * 100, 2)
        }

    except HTTPException:
        raise

    except Exception:
        logger.exception("Resume matching failed")

        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while processing the resume."
        )

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)