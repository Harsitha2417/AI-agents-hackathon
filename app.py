import streamlit as st

from tools.resume_tool import screen_resume
from tools.jd_tool import improve_job_description
from tools.interview_tool import generate_interview_questions
from tools.email_tool import generate_email
from tools.salary_tool import get_salary

st.set_page_config(
    page_title="SmartHire AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 SmartHire AI")
st.subheader("Agentic Recruitment Assistant")

st.sidebar.title("Choose Feature")

feature = st.sidebar.radio(
    "Select",
    (
        "Resume Screening",
        "Improve Job Description",
        "Interview Questions",
        "Salary Benchmark",
        "Candidate Email"
    )
)

# -----------------------------------------
# Resume Screening
# -----------------------------------------

if feature == "Resume Screening":

    st.header("Resume Screening")

    resume = st.text_area(
        "Paste Resume Here",
        height=300
    )

    if st.button("Analyze Resume"):

        if resume.strip() == "":
            st.warning("Please paste a resume.")
        else:

            with st.spinner("Analyzing Resume..."):

                result = screen_resume(resume)

            st.success("Analysis Completed")

            st.write(result)

# -----------------------------------------
# Improve Job Description
# -----------------------------------------

elif feature == "Improve Job Description":

    st.header("Improve Job Description")

    jd = st.text_area(
        "Paste Job Description",
        height=300
    )

    if st.button("Improve JD"):

        if jd.strip() == "":
            st.warning("Please enter a Job Description.")
        else:

            with st.spinner("Improving Job Description..."):

                result = improve_job_description(jd)

            st.success("Completed")

            st.write(result)

# -----------------------------------------
# Interview Questions
# -----------------------------------------

elif feature == "Interview Questions":

    st.header("Generate Interview Questions")

    role = st.text_input("Job Role")

    if st.button("Generate Questions"):

        if role.strip() == "":
            st.warning("Please enter a role.")
        else:

            with st.spinner("Generating Questions..."):

                result = generate_interview_questions(role)

            st.success("Completed")

            st.write(result)

# -----------------------------------------
# Salary Benchmark
# -----------------------------------------

elif feature == "Salary Benchmark":

    st.header("Salary Benchmark")

    role = st.text_input("Role")

    city = st.text_input("City")

    if st.button("Find Salary"):

        if role == "" or city == "":
            st.warning("Enter Role and City")
        else:

            salary = get_salary(role, city)

            st.success("Salary Found")

            st.write(f"### Average Salary : {salary}")

# -----------------------------------------
# Candidate Email
# -----------------------------------------

elif feature == "Candidate Email":

    st.header("Generate Candidate Email")

    candidate = st.text_input("Candidate Name")

    role = st.text_input("Role")

    email_type = st.selectbox(
        "Email Type",
        [
            "Interview Invitation",
            "Offer Letter",
            "Rejection Email"
        ]
    )

    st.warning("Human Confirmation Required")

    confirm = st.checkbox(
        "I confirm generating this email."
    )

    if st.button("Generate Email"):

        if not confirm:

            st.error("Please confirm before continuing.")

        else:

            with st.spinner("Generating Email..."):

                result = generate_email(
                    candidate,
                    role,
                    email_type
                )

            st.success("Completed")

            st.write(result)