import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_email(candidate_name, role, email_type):
    """
    Generate professional recruitment emails.

    email_type:
    - Interview Invitation
    - Offer Letter
    - Rejection Email
    """

    prompt = f"""
You are an HR Manager.

Generate a professional recruitment email.

Candidate Name: {candidate_name}

Job Role: {role}

Email Type: {email_type}

Instructions:
- Keep the email professional.
- Use a polite tone.
- Add a subject line.
- Include greeting and closing.
- Do not use markdown.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# ------------------------
# Testing
# ------------------------

if __name__ == "__main__":

    result = generate_email(
        candidate_name="Rahul Sharma",
        role="Backend Developer",
        email_type="Interview Invitation"
    )

    print(result)