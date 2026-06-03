import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Internship Application Agent")

st.title("AI Internship Application Agent")
st.write("An agentic AI assistant for Data Science and Generative AI internship applications.")

resume = st.text_area("Paste your resume here", height=220)
job_description = st.text_area("Paste the job description here", height=220)

user_goal = st.text_input(
    "What do you need help with?",
    "I want help applying for this internship."
)

system_prompt = """
You are an AI Internship Application Agent for students applying to Data Science,
Machine Learning, and Generative AI internships.

Rules:
- Be honest and specific.
- Do not invent experience.
- Use only the resume, job description, and skill framework.
- If information is missing, explain what is missing.
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
- TensorFlow
- PyTorch
- GitHub
- Streamlit
- Generative AI
- Prompt Engineering
- API Integration
- Communication
- Problem Solving
"""

def build_prompt(user_goal, resume, job_description):
    return f"""
{system_prompt}

User Goal:
{user_goal}

Grounding Skill Framework:
{skill_framework}

Resume:
{resume}

Job Description:
{job_description}

Available Agent Tools:

1. Analyze Job Fit
   - Compare resume and job description
   - Generate match score
   - Identify missing skills

2. Improve Resume Bullets
   - Rewrite resume bullets
   - Use stronger action verbs
   - Do not invent experience

3. Write Recruiter Message
   - Create a recruiter outreach message
   - Keep it professional and concise

4. Generate Interview Prep
   - Generate interview questions
   - Include preparation advice

5. Create Application Checklist
   - Create a checklist before applying

Your Task:

Step 1:
Decide which tool is most appropriate for the user's goal.

Step 2:
Explain why that tool was selected.

Step 3:
Execute the tool.

Step 4:
Provide the final result.

Use the following format:

Selected Tool:
Reason:
Output:
Recommendations:
"""
    
if st.button("Run Agent"):
    if not resume or not job_description:
        st.warning("Please paste both resume and job description.")
    else:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

        model = genai.GenerativeModel("gemini-2.5-flash-lite")

        prompt = build_prompt(
            user_goal,
            resume,
            job_description
        )

        with st.spinner("Agent is working..."):
            response = model.generate_content(prompt)

        st.subheader("Agent Output")
        st.write(response.text)
