# Evaluation Examples

## What Good Looks Like

A good output should:
- Use the resume and job description correctly
- Not invent experience
- Identify matching and missing skills
- Give useful next steps
- Follow the selected agent action

## Test Case 1: Strong Data Analyst Match

Resume:
Python, SQL, Excel, Tableau, Data Analysis project experience

Job:
Data Analyst Intern requiring Python, SQL, Excel, Tableau

Expected:
High match score and strong skill match.

Actual:
To be tested.

## Test Case 2: Weak AI Role Match

Resume:
Customer service experience, basic Excel

Job:
Machine Learning Intern requiring Python, ML, Scikit-learn, model evaluation

Expected:
Low match score and clear missing skills.

Actual:
To be tested.

## Test Case 3: Missing Job Description Details

Resume:
Python, SQL, statistics, dashboard project

Job:
We are hiring an intern.

Expected:
The agent should say there is not enough job information.

Actual:
To be tested.

## Test Case 4: Resume Unrelated to Job

Resume:
Retail cashier, customer support, scheduling

Job:
Data Science Intern requiring Python, SQL, machine learning

Expected:
Low match score and suggestions for projects/skills to build.

Actual:
To be tested.

## Test Case 5: Good Resume Missing Tools

Resume:
Python, SQL, statistics, machine learning

Job:
BI Intern requiring Power BI, Tableau, Excel, SQL

Expected:
Medium match score with missing visualization tools.

Actual:
To be tested.
