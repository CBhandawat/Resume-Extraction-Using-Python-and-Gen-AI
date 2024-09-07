# Resume-Extraction-Using-Python-and-Gen-AI

# THIS REPOSITORY HOLDS AS FOLLOWS:
1. THE FILES FOR STREAMLIT APPLICATION MADE FOR RESUME EXTRACTION <br>
2. THE PYTHON CODE MADE IN GOOGLE COLAB

# Summary
As the name suggests Resume Extraction enables you to extract information in JSON format from your resume(for extensions like: .pdf, .txt, .docx) using Large Language Model GPT(gpt-4o-mini). The information it extracts are as follows:<br>

•	Name <br>
•	Contact Information (Email, Phone Number) <br>
•	Professional Summary <br>
•	Work Experience <br>
•	Education <br>
•	Skills <br>
•	Certifications

It also handle cases where specific sections (e.g., Certifications) might be missingand implement fallback mechanisms if the AI model fails to extract certain details.

# DEMO

[streamlit-resume_extraction-2024-09-07-11-09-81.webm](https://github.com/user-attachments/assets/110ae4de-6c42-4997-966a-329426340a3a)


# Getting Started
1. Prerequisites:
  a. 3.11 ≤ Python < 3.12.5 <br/>
  b. [OpenAI API Key](https://auth.openai.com/authorize?issuer=auth0.openai.com&client_id=DRivsnm2Mu42T3KOpqdtwB3NYviHYzwD&audience=https%3A%2F%2Fapi.openai.com%2Fv1&redirect_uri=https%3A%2F%2Fplatform.openai.com%2Fauth%2Fcallback&device_id=89fec6e2-ceef-4aa9-9a00-c861166971f4&screen_hint=signup&max_age=0&scope=openid+profile+email+offline_access&response_type=code&response_mode=query&state=Q18waFZoY2owbTJ0NUgybnE3MkdUM0NzQW8wTnkyQzYzOGpyYldDZFE3MQ%3D%3D&nonce=VG1sSUNaTU4ydVcxd0c2Vm52c084RmlSbjlVVVRmWEFYMlhFWmN2ajAxQg%3D%3D&code_challenge=7q-RHFsluPgm1sUtF7_sMyoItqfd__7wnDYs6d1n4gY&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtc3BhLWpzIiwidmVyc2lvbiI6IjEuMjEuMCJ9&flow=control) <br/>
  c. The documents <br/>

2. Clone the repository
    ```
    git clone https://github.com/CBhandawat/Resume-Extraction-Using-Python-and-Gen-AI
    cd Resume-Extraction-Using-Python-and-Gen-AI
    ```

3. Setup
   Create Virtual Environment:
     ```
     python -m venv .venv
     ```

   Activate:
     ```
     .venv\scripts\activate
     ```

   Install all requirements:
     ```
     pip install -r requirements.txt
     ```

4. Run
   ```
   streamlit run resume_extraction.py
   ```
It will open your browser and from there you can enter your OPENAI API KEY and get started.

# Acknowledgement
Special thanks to [Streamlit](https://github.com/streamlit/streamlit) for their invaluable contributions to the open source community. 

# LICENSE
[Apache 2.0 License](https://github.com/CBhandawat/Resume-Extraction-Using-Python-and-Gen-AI/blob/main/LICENSE)
