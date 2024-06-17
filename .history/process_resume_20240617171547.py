import pandas as pd
import sys
import nltk
import pdfplumber
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz
import spacy

# Initialize spaCy model
nlp = spacy.load('en_core_web_sm')

def process_resume(resume_text, job_requirements):
    doc = nlp(resume_text)
    
    # Extracting name and phone number
    name = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    phone_number = [token.text for token in doc if token.like_num and len(token.text) == 10]

    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(resume_text)
    filtered_tokens = [w for w in tokens if not w.lower() in stop_words and w.isalnum()]

    skill_match = [fuzz.token_set_ratio(skill, job_requirements) for skill in filtered_tokens]
    match_percentage = sum(skill_match) / len(filtered_tokens) * 100 if filtered_tokens else 0

    # Create a DataFrame with the extracted data
    data = {
        'Name': name[0] if name else 'N/A',
        'Phone Number': phone_number[0] if phone_number else 'N/A',
        'Skills': ', '.join(filtered_tokens),
        'Match Percentage': match_percentage
    }

    df = pd.DataFrame([data])
    return df

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python process_resume.py <resume_text> <job_requirements>")
        sys.exit(1)

    resume_text = sys.argv[1]
    job_requirements = sys.argv[2]

    try:
        result_df = process_resume(resume_text, job_requirements)
        print(result_df.to_string(index=False))  # Print the DataFrame as a table
    except Exception as e:
        print(f"Error processing resume: {e}", file=sys.stderr)
        sys.exit(1)
