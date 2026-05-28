import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Internship Application Agent")

st.title("AI Internship Application Agent")
st.write("An agentic AI assistant for Data Science and Generative AI internship applications.")

resume = st.text_area("Paste your resume here", height=220)
job_description = st.text_area("Paste the job description here", height=220)

action = st.selectbox(
    "Choose what action the agent should take",
    [
        "Analyze Job Fit",
        "Improve Resume Bullets",
        "Write Recruiter Message",
        "Generate Interview Prep",
        "Create Application Checklist"
    ]
)

system_prompt = """
You are an agentic AI career assistant for students applying to Data Science,
Machine Learning, and Generative AI internships.

You can perform different actions depending on the user's selected goal.

Rules:
- Be honest and specific.
- Do not invent experience.
- Use only the resume, job description, and provided skill framework.
- If information is missing, say what is missing.
- Give practical next steps.
- Focus on internships and early-career candidates.
"""

skill_framework = """
Data Science and AI internship skill framework:
- Python
- SQL
- R
- Statistics
- Machine Learning
- Data Cleaning
- Data Visualization
- Excel
- Tableau
- Power BI
- Pandas
- NumPy
- Scikit-learn
- TensorFlow or PyTorch
- GitHub
- Streamlit
- Generative AI
- Prompt Engineering
- API Integration
- Communication
- Problem Solving
"""

def build_prompt(action, resume, job_description):
    return f"""
{system_prompt}

Selected Agent Action:
{action}

Grounding Skill Framework:
{skill_framework}

Resume:
{resume}

Job Description:
{job_description}

Instructions:
If the selected action is Analyze Job Fit:
- Give match score out of 100.
- Explain strongest matches.
- Explain missing skills.
- Recommend 3 improvement steps.

If the selected action is Improve Resume Bullets:
- Rewrite 5 resume bullets for this job.
- Do not invent experience.
- Use stronger action verbs.
- Keep bullets realistic for a student/intern.

If the selected action is Write Recruiter Message:
- Write a short LinkedIn or email message to a recruiter.
- Mention the role and relevant skills.
- Keep it professional and simple.

If the selected action is Generate Interview Prep:
- Create 8 interview questions.
- Include simple preparation tips.
- Include technical and behavioral questions.

If the selected action is Create Application Checklist:
- Create a checklist of steps before applying.
- Include resume, skills, projects, GitHub, and interview preparation.

Return the answer in clear sections.
"""

if st.button("Run Agent"):
    if not resume or not job_description:
        st.warning("Please paste both resume and job description.")
    else:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-2.5-flash-lite")

        prompt = build_prompt(action, resume, job_description)

        with st.spinner("Agent is working..."):
            response = model.generate_content(prompt)

        st.subheader("Agent Output")
        st.write(response.text)
