import openai
from openai import AuthenticationError
import streamlit as st

def read_document(file):
    """
    Read file of the format .pdf, .docx and .txt and returns the data of that file.

    Args:
        file: Resume from which the information has to be extracted.

    Returns:
        data: text content of the resume
    """

    name, extension = os.path.splitext(file)

    # PDF file loader using pypdf
    if extension == '.pdf':
        from pypdf import PdfReader
        reader = PdfReader(file)
        data = ""
        for page in reader.pages:
            data += page.extract_text()

    # DOCX file loader using python-docx
    elif extension == '.docx':
        from docx import Document
        doc = Document(file)
        data = "\n".join([para.text for para in doc.paragraphs])

    # TXT file loader using built-in open
    elif extension == '.txt':    
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()

    else:
        print('Document format not supported!')
        return None

    return data



def extractor(resume_data):
    """
    Extracts information from the resume_data using 'gpt-4o-mini' and returns it in JSON format.

    Args:
        resume_data (str): The text content of the resume.

    Returns:
        extracted_data: containing the extracted information in json format.
    """

    prompt = '''
    You are an AI bot designed to act as a professional for parsing resumes. You are given a resume and your job is to extract the following information from the resume:
    1. Name
    2. Contact Information (Email, Phone Number)
    3. Professional Summary
    4. Work Experience
    5. Education
    6. Skills
    7. Certifications

    Provide the extracted information in JSON format.

    If the file does not contain any information, return the fallback message: "Sorry, it seems this is not a resume. Try uploading a different file.".

    If the file does not contain some of the sections, then do not request further information for that and apart from the information print the message: "It seems some of the information is missing from the resume"

    REMEMBER YOU ARE NOT CAPABLE OF SOLVING ANY OTHER QUERIES AND MESSAGES ARE NOT PART OF JSON FORMAT.
    '''
    
    # Initialize OpenAI client (assuming correct API key handling)
    client = openai.OpenAI()
    user_content = resume_data
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_content}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.0,
        max_tokens=1500
    )
    
    # Extract content from the response
    extracted_data = response.choices[0].message.content
    
    return extracted_data




def check_api_key(api_key):
    """
    Checks if the OPENAI API KEY is correct or not.

    Args:
        api_key: OPENAI API KEY

    Returns: 
        True: for correct API KEY
        False: for incorrect API KEY
    """

    try:
        openai.api_key = api_key
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "test"}],  # Minimal prompt
            max_tokens=1,  # Limit response length
        )
        st.success('Valid API Key!')  # API key is valid
        return True
    except AuthenticationError as e:
        st.error('Invalid API Key! Please check and try again.')
        return False
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False
    

if __name__ == "__main__":
  import os
  from dotenv import load_dotenv, find_dotenv
  load_dotenv(find_dotenv(), override=True)

  
  st.subheader('Resume Extraction with Python and Gen AI')

  # Enter the OPENAI API KEY
  api_key = st.text_input('ENTER YOUR OPEN_AI_API_KEY:',type='password')
  response = False
  # Checking if the API KEY entered is correct
  if api_key:
    os.environ['OPENAI_API_KEY'] = api_key
    response = check_api_key(api_key)

  # Upload a Resume from which the information needs to be extracted.
  uploaded_file = st.file_uploader('Upload a Resume',type=['pdf','docx','txt'], disabled=not response)
  
  # Reading resume and extracting information
  if uploaded_file:
    with st.spinner("Reading Resume..."):
        bytes_data=uploaded_file.read()
        file_name = os.path.join('./',uploaded_file.name)
        with open(file_name, 'wb') as f:
            f.write(bytes_data)

        data = read_document(file_name)
        # st.write(type(data))
        st.success('Resume Uploaded Successfully.')
    with st.spinner("Extracting Information..."):
        extracted_data = extractor(data)

        if extracted_data:
          st.text_area('Extracted Information: ', value=extracted_data)
