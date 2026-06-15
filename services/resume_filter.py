from .pdf_service import extract_text
import re


# Sections to KEEP for matching
RELEVANT_SECTIONS = [

    # Summary
    "summary",
    "professional summary",
    "executive summary",
    "career summary",
    "profile",
    "professional profile",
    "candidate profile",
    "overview",
    "career overview",
    "professional overview",
    "about me",
    "objective",
    "career objective",

    # Experience
    "experience",
    "work experience",
    "professional experience",
    "employment",
    "employment history",
    "work history",
    "career history",
    "industry experience",
    "internship",
    "internships",
    "internship experience",
    "apprenticeship",
    "job experience",
    "relevant experience",

    # Skills
    "skills",
    "technical skills",
    "core skills",
    "key skills",
    "professional skills",
    "technical expertise",
    "competencies",
    "core competencies",
    "areas of expertise",
    "expertise",
    "technologies",
    "technology stack",
    "tech stack",
    "technical proficiencies",
    "proficiencies",
    "programming skills",
    "software skills",
    "tools",
    "tools & technologies",
    "tools and technologies",

    # Projects
    "projects",
    "project experience",
    "academic projects",
    "professional projects",
    "key projects",
    "major projects",
    "personal projects",
    "capstone project",
    "capstone projects",
    "research projects",

    # Certifications
    "certifications",
    "certification",
    "certificates",
    "training",
    "professional training",
    "courses",
    "completed courses",
    "licenses",
    "licenses & certifications",
    "credentials",

    # Achievements
    "achievements",
    "accomplishments",
    "key achievements",
    "professional achievements",
    "awards",
    "honors",
    "recognitions",

    # Publications / Research
    "research",
    "research work",
    "publications",
    "papers",
    "journal publications",
    "conference publications",

    # Open Source
    "open source",
    "open source contributions",
    "community contributions",

    # Leadership
    "leadership",
    "leadership experience",
    "positions of responsibility",
    "responsibilities",

    # Domain Specific
    "trading experience",
    "machine learning experience",
    "software development",
    "development experience",
    "engineering experience",
    "technical experience"
]

# Sections to DISCARD
IRRELEVANT_SECTIONS = [

    # Education
    "education",
    "academic background",
    "academic qualifications",
    "qualifications",
    "schooling",
    "university",
    "college",
    "academic history",

    # Personal Information
    "personal information",
    "personal details",
    "personal profile",
    "personal data",
    "bio",
    "about me",
    "about",
    "profile details",

    # Contact
    "contact",
    "contact information",
    "contact details",
    "address",
    "email",
    "phone",
    "mobile",
    "linkedin",
    "github",
    "portfolio",

    # References
    "references",
    "reference",
    "professional references",

    # Hobbies
    "hobbies",
    "interests",
    "personal interests",
    "extracurricular activities",
    "activities",
    "leisure activities",

    # Languages
    "languages",
    "language proficiency",
    "spoken languages",

    # Declaration
    "declaration",
    "self declaration",

    # Family
    "family details",
    "father name",
    "mother name",
    "marital status",
    "nationality",
    "gender",
    "date of birth",
    "dob",

    # Miscellaneous
    "strengths",
    "weaknesses",
    "objective statement",
    "career goal",
    "career goals",
    "personal objective",

    # Government Resume Sections
    "signature",
    "place",
    "date",
    "passport details",
    "identity details",

    # ATS Noise
    "table of contents",
    "index",
    "appendix",
    "annexure",
    "attachments",

    # Social Links
    "social media",
    "social profiles",
    "online presence"
]



class Resume:

    @staticmethod
    def extract_sections(resume_text: str) -> dict:
        """Split resume into sections by detecting headers."""
        sections = {}
        current_section = "header"
        current_content = []
        
        for line in resume_text.split('\n'):
            # Detect section headers (short lines, often ALL CAPS or Title Case)
            stripped = line.strip()
            if stripped and len(stripped) < 40 and stripped.replace(' ', '').isalpha():
                if current_content:
                    sections[current_section] = '\n'.join(current_content)
                current_section = stripped.lower()
                current_content = []
            else:
                current_content.append(line)
        
        if current_content:
            sections[current_section] = '\n'.join(current_content)
        
        return sections

    @staticmethod
    def  filter_relevant_sections(resume_text: str) -> str:
        """Keep only job-relevant sections for embedding."""
        sections = Resume.extract_sections(resume_text)
        
        relevant_text = []
        for section_name, content in sections.items():
            is_relevant = any(kw in section_name for kw in RELEVANT_SECTIONS)
            is_irrelevant = any(kw in section_name for kw in IRRELEVANT_SECTIONS)
            
            if is_relevant and not is_irrelevant:
                relevant_text.append(content)
        
        return '\n'.join(relevant_text)


if __name__=="__main__":

    file_path = r"test\files_for_test\Kondapalli_CV_2026.pdf"
    r_text =extract_text (file_path)
    res_relavent_text =  Resume.filter_relevant_sections(r_text)
    print(f"size of text before filter : {len(r_text)}")
    print(f"size of text after filter : {len(res_relavent_text)}")
    print(f"filtered text : {res_relavent_text}")


    




