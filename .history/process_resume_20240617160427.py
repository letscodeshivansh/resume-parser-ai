import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import json
import nltk
import pdfplumber

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

import spacy
from fuzzywuzzy import fuzz
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer


# ciwith pdfplumber.open('resume.pdf') as pdf:
    text = ''
    for page in pdf.pages:
        resume_text += page.extract_text()
        

nlp = spacy.load('en_core_web_sm')

doc = nlp(text)
name = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
phone_number = [token.text for token in doc if token.like_num and len(token.text) == 10]

stop_words = set(stopwords.words('english'))
tokens = word_tokenize(text)
filtered_tokens = [w for w in tokens if not w.lower() in stop_words and w.isalnum()]


job_requirements = "Python, Machine Learning, Data Analysis"
skill_match = [fuzz.token_set_ratio(skill, job_requirements) for skill in filtered_tokens]
match_percentage = sum(skill_match) / len(filtered_tokens) * 100


data = {
    'Name': name[0] if name else 'N/A',
    'Phone Number': phone_number[0] if phone_number else 'N/A',
    'Skills': filtered_tokens,
    'Match Percentage': match_percentage
}

df = pd.DataFrame([data])
sns.barplot(x='Skills', y='Match Percentage', data=df)
plt.show()


        
def process_resume(resume_text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(resume_text)
    filtered_text = [w for w in word_tokens if w.lower() not in stop_words and w.isalnum()]

    freq_dist = FreqDist(filtered_text)
    common_words = freq_dist.most_common(10)
    
    return common_words


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_resume.py <resume_text>")
        sys.exit(1)

    resume_text = sys.argv[1]

    try:
        result = process_resume(resume_text)
        print(json.dumps(result))
    except Exception as e:
        print(f"Error processing resume: {e}", file=sys.stderr)
        sys.exit(1)
