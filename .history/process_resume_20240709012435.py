import os
import numpy as np
import pandas as pd
import spacy
import pickle
import random
import fitz
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from IPython.display import FileLinks
import sys
import nltk
import pdfplumber
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz

# Initialize spaCy model
nlp = spacy.load('en_core_web_sm')

# Process resume text
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

    # Create a data dictionary with the extracted data
    data = {
        'Name': name[0] if name else 'N/A',
        'Phone Number': phone_number[0] if phone_number else 'N/A',
        'Skills': ', '.join(filtered_tokens),
        'Match Percentage': f"{match_percentage:.2f}%"
    }

    return data

# Function to load and process PDF file
def load_pdf(file_path):
    with fitz.open(file_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return " ".join(text.split('\n'))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python process_resume.py <resume_pdf_path> <job_requirements>")
        sys.exit(1)

    file_path = sys.argv[1]
    job_requirements = sys.argv[2]

    resume_text = load_pdf(file_path)

    try:
        result = process_resume(resume_text, job_requirements)
        print(result)
    except Exception as e:
        print(f"Error processing resume: {e}", file=sys.stderr)
        sys.exit(1)

# Evaluation Metrics
true_labels = ['Name', 'Phone Number', 'Skills', 'Match Percentage']

# Assuming some true data for evaluation, this should be replaced by actual true data in practice
true_data = {
    'Name': 'John Doe',
    'Phone Number': '1234567890',
    'Skills': 'Python, Machine Learning, Data Analysis',
    'Match Percentage': '85.00%'
}

predicted_labels_list = list(result.keys())
predicted_values_list = list(result.values())
true_values_list = list(true_data.values())

# Compute confusion matrix
conf_matrix = confusion_matrix(true_values_list, predicted_values_list, labels=true_values_list)

# Compute accuracy
accuracy = accuracy_score(true_values_list, predicted_values_list)

# Compute precision
precision = precision_score(true_values_list, predicted_values_list, average='weighted')

# Compute recall
recall = recall_score(true_values_list, predicted_values_list, average='weighted')

# Compute F1-score
f1 = f1_score(true_values_list, predicted_values_list, average='weighted')

# Generate classification report
report = classification_report(true_values_list, predicted_values_list)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print("Classification Report:\n", report)
print("Confusion Matrix:\n", conf_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=true_labels, yticklabels=true_labels)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

# Metrics names
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-score']

# Corresponding metric values
values = [accuracy, precision, recall, f1]

# Plotting the metrics
plt.figure(figsize=(8, 5))
sns.barplot(x=metrics, y=values, palette='viridis')
plt.ylim(0, 1)
plt.title('Classification Metrics')
plt.ylabel('Score')
plt.show()

FileLinks(r'nlp_ner_model')
