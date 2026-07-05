import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def improve_job_description(job_description):

    prompt = f"""
You are an experienced HR Manager.

Rewrite the following Job Description professionally.

Include:

1. Job Title
2. Job Summary
3. Responsibilities
4. Required Skills
5. Qualifications
6. Preferred Skills

Job Description:

{job_description}
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

    jd = """
Need Python developer.

Should know Python.

Freshers can apply.
"""

    print(improve_job_description(jd))