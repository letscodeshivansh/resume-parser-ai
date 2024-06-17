import sys
import json
import nltk
import pdfplumber

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def process_resume(resume_text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(resume_text)
    filtered_text = [w for w in word_tokens if w.lower() not in stop_words and w.isalnum()]

    freq_dist = FreqDist(filtered_text)
    common_words = freq_dist.most_common(10)
    return common_words


import pdfplumber

with pdfplumber.open('resume.pdf') as pdf:
    text = ''
    for page in pdf.pages:
        text += page.extract_text()

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
