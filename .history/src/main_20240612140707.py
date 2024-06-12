# process_resume.py
import sys
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token.lower() not in stopwords.words('english')]
    return tokens

if __name__ == "__main__":
    resume_text = sys.argv[1]
    processed_tokens = preprocess_text(resume_text)
    print(json.dumps(processed_tokens))
