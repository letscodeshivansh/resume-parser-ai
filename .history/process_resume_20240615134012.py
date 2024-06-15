import sys
import json
import nltk
import pdfplumber

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def process_resume(resume_text):
    # Basic text processing
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(resume_text)
    filtered_text = [w for w in word_tokens if w.lower() not in stop_words and w.isalnum()]

    # Frequency distribution of words
    freq_dist = FreqDist(filtered_text)

    # Example output: top 10 most common words
    common_words = freq_dist.most_common(10)

    return common_words

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_resume.py <resume_text>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    try:
        resume_text = extract_text_from_pdf(pdf_path)
        result = process_resume(resume_text)
        print(json.dumps(result))
    except Exception as e:
        print(f"Error processing resume: {e}", file=sys.stderr)
        sys.exit(1)
