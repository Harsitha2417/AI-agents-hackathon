import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def screen_resume(resume_text):

    prompt = f"""
You are an experienced HR Manager.

Analyze the following resume.

Return your answer in this format:

Resume Score (Out of 10)

Skills Found

Experience

Education

Strengths

Missing Skills

Recommendation

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -------------------------
# Testing
# -------------------------

if __name__ == "__main__":

    sample_resume = """
John Doe

Skills:
Python
Java
SQL
Git

Experience:
2 Years

Education:
B.Tech Computer Science

Projects:
Hospital Management System
Employee Portal
"""

    result = screen_resume(sample_resume)

    print(result)