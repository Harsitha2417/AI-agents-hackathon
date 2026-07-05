import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_interview_questions(role):

    prompt = f"""
You are an experienced Technical Interviewer.

Generate 10 interview questions for the following role.

Role:

{role}

Questions should contain:

Easy Questions

Medium Questions

Advanced Questions
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -----------------------
# Testing
# -----------------------

if __name__ == "__main__":

    print(generate_interview_questions("Backend Developer"))