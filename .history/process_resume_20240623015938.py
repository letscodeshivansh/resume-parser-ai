
import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import spacy
import pickle
import random

# List all files under the input directory
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

train_data = pickle.load(open('/kaggle/input/resume-data-with-annotations/train_data.pkl','rb'))
train_data[0]

# Load Blank Model
nlp = spacy.blank('en')

def train_model(train_data):
    # Remove all pipelines and add NER pipeline from the model
    if 'ner'not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        # adding NER pipeline to nlp model
        nlp.add_pipe(ner,last=True)
    
    #Add labels in the NLP pipeline
    for _, annotation in train_data:
        for ent in annotation.get('entities'):
            ner.add_label(ent[2])
    
    #Remove other pipelines if they are there
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(10): # train for 10 iterations
            print("Starting iteration " + str(itn))
            random.shuffle(train_data)
            losses = {}
            index = 0
            for text, annotations in train_data:
                try:
                    nlp.update(
                        [text],  # batch of texts
                        [annotations],  # batch of annotations
                        drop=0.2,  # dropout - make it harder to memorise data
                        sgd=optimizer,  # callable to update weights
                        losses=losses)
                except Exception as e:
                    pass
                
            print(losses)
# Start Training model
train_model(train_data)
        

# Saving the model
nlp.to_disk('nlp_ner_model')
#Loading Model
nlp_model = spacy.load('nlp_ner_model')
# trying and seeing the prediction of the model
doc = nlp_model(train_data[0][0])
for ent in doc.ents:
    print(f"{ent.label_.upper():{30}}-{ent.text}")
NAME                          -Samyuktha Shivakumar
LOCATION                      -Bangalore
EMAIL ADDRESS                 -indeed.com/r/Samyuktha-Shivakumar/ cabce09fe942cb85
!pip install PyMuPDF 
Requirement already satisfied: PyMuPDF in /opt/conda/lib/python3.7/site-packages (1.22.5)
WARNING: You are using pip version 20.2.4; however, version 24.0 is available.
You should consider upgrading via the '/opt/conda/bin/python3.7 -m pip install --upgrade pip' command.
import fitz

file_path = input("Enter the path to the PDF file: ").strip()
if not file_path:
    print("Please provide a valid file path.")
else:
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text()
    tx = " ".join(text.split('\n'))
    print(tx)
Alice Clark  AI / Machine Learning    Delhi, India Email me on Indeed  •  20+ years of experience in data handling, design, and development  •  Data Warehouse: Data analysis, star/snow flake scema data modelling and design specific to  data warehousing and business intelligence  •  Database: Experience in database designing, scalability, back-up and recovery, writing and  optimizing SQL code and Stored Procedures, creating functions, views, triggers and indexes.  Cloud platform: Worked on Microsoft Azure cloud services like Document DB, SQL Azure,  Stream Analytics, Event hub, Power BI, Web Job, Web App, Power BI, Azure data lake  analytics(U-SQL)  Willing to relocate anywhere    WORK EXPERIENCE  Software Engineer  Microsoft – Bangalore, Karnataka  January 2000 to Present  1. Microsoft Rewards Live dashboards:  Description: - Microsoft rewards is loyalty program that rewards Users for browsing and shopping  online. Microsoft Rewards members can earn points when searching with Bing, browsing with  Microsoft Edge and making purchases at the Xbox Store, the Windows Store and the Microsoft  Store. Plus, user can pick up bonus points for taking daily quizzes and tours on the Microsoft  rewards website. Rewards live dashboards gives a live picture of usage world-wide and by  markets like US, Canada, Australia, new user registration count, top/bottom performing rewards  offers, orders stats and weekly trends of user activities, orders and new user registrations. the  PBI tiles gets refreshed in different frequencies starting from 5 seconds to 30 minutes.  Technology/Tools used    EDUCATION  Indian Institute of Technology – Mumbai  2001    SKILLS  Machine Learning, Natural Language Processing, and Big Data Handling    ADDITIONAL INFORMATION  Professional Skills  • Excellent analytical, problem solving, communication, knowledge transfer and interpersonal  skills with ability to interact with individuals at all the levels  • Quick learner and maintains cordial relationship with project manager and team members and  good performer both in team and independent job environments  • Positive attitude towards superiors &amp; peers  • Supervised junior developers throughout project lifecycle and provided technical assistance  
# Applying the model
doc = nlp_model(tx)
for ent in doc.ents:
    print(f'{ent.label_.upper():{30}}- {ent.text}')
NAME                          - Alice Clark
LOCATION                      - Delhi
DESIGNATION                   - Software Engineer
COMPANIES WORKED AT           - Microsoft
COMPANIES WORKED AT           - Microsoft
COMPANIES WORKED AT           - Microsoft
COMPANIES WORKED AT           - Microsoft
COMPANIES WORKED AT           - Microsoft
COLLEGE NAME                  - Indian Institute of Technology – Mumbai
SKILLS                        - Machine Learning, Natural Language Processing, and Big Data Handling
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# True labels
true_labels = ['COLLEGE NAME', 'COMPANIES WORKED AT', 'NAME', 'SKILLS', 'LOCATION', 'DESIGNATION']

def extract_predicted_labels_from_entities(entities):
    predicted_labels = set()  # Initialize an empty set to store predicted labels
    # Loop through the entities
    for ent in entities:
        predicted_labels.add(ent.label_.upper())  # Add the label to the set
    return list(predicted_labels)  # Convert set to list


# Example usage:
predicted_labels_list = extract_predicted_labels_from_entities(doc.ents)
print(predicted_labels_list)
# Compute confusion matrix
conf_matrix = confusion_matrix(true_labels, predicted_labels_list)

# Compute accuracy
accuracy = accuracy_score(true_labels, predicted_labels_list)

# Compute precision
precision = precision_score(true_labels, predicted_labels_list, average='weighted')

# Compute recall
recall = recall_score(true_labels, predicted_labels_list, average='weighted')

# Compute F1-score
f1 = f1_score(true_labels, predicted_labels_list, average='weighted')

# Generate classification report
report = classification_report(true_labels, predicted_labels_list)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print("Classification Report:\n", report)
print("Confusion Matrix:\n", conf_matrix)
['COLLEGE NAME', 'COMPANIES WORKED AT', 'NAME', 'SKILLS', 'LOCATION', 'DESIGNATION']
Accuracy: 1.0
Precision: 1.0
Recall: 1.0
F1-score: 1.0
Classification Report:
                      precision    recall  f1-score   support

       COLLEGE NAME       1.00      1.00      1.00         1
COMPANIES WORKED AT       1.00      1.00      1.00         1
        DESIGNATION       1.00      1.00      1.00         1
           LOCATION       1.00      1.00      1.00         1
               NAME       1.00      1.00      1.00         1
             SKILLS       1.00      1.00      1.00         1

           accuracy                           1.00         6
          macro avg       1.00      1.00      1.00         6
       weighted avg       1.00      1.00      1.00         6

Confusion Matrix:
 [[1 0 0 0 0 0]
 [0 1 0 0 0 0]
 [0 0 1 0 0 0]
 [0 0 0 1 0 0]
 [0 0 0 0 1 0]
 [0 0 0 0 0 1]]
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

from IPython.display import FileLinks
FileLinks(r'nlp_ner_model')
nlp_ner_model/
  meta.json
  tokenizer
nlp_ner_model/ner/
  model
  moves
  cfg
nlp_ner_model/vocab/
  lookups.bin
  vectors
  key2row
  strings.json
         
        
        