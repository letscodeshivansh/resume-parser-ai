
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
/kaggle/input/resume-data-with-annotations/resume v6.pdf
/kaggle/input/resume-data-with-annotations/Alice Clark CV.docx
/kaggle/input/resume-data-with-annotations/Alice Clark CV.txt
/kaggle/input/resume-data-with-annotations/AshlyLauResume.pdf
/kaggle/input/resume-data-with-annotations/Smith Resume.pdf
/kaggle/input/resume-data-with-annotations/train_data.txt
/kaggle/input/resume-data-with-annotations/Smith Resume.docx
/kaggle/input/resume-data-with-annotations/Jinesh_Dhruv_poster.pdf
/kaggle/input/resume-data-with-annotations/Alice Clark CV.pdf
/kaggle/input/resume-data-with-annotations/train_data.pkl
/kaggle/input/resume-data-with-annotations/Sample_Resume.pdf
/kaggle/input/resume-data-with-annotations/Xinni_Chng.pdf
/kaggle/input/resume-data-with-annotations/sample_input.pdf
train_data = pickle.load(open('/kaggle/input/resume-data-with-annotations/train_data.pkl','rb'))
train_data[0]
('Govardhana K Senior Software Engineer  Bengaluru, Karnataka, Karnataka - Email me on Indeed: indeed.com/r/Govardhana-K/ b2de315d95905b68  Total IT experience 5 Years 6 Months Cloud Lending Solutions INC 4 Month • Salesforce Developer Oracle 5 Years 2 Month • Core Java Developer Languages Core Java, Go Lang Oracle PL-SQL programming, Sales Force Developer with APEX.  Designations & Promotions  Willing to relocate: Anywhere  WORK EXPERIENCE  Senior Software Engineer  Cloud Lending Solutions -  Bangalore, Karnataka -  January 2018 to Present  Present  Senior Consultant  Oracle -  Bangalore, Karnataka -  November 2016 to December 2017  Staff Consultant  Oracle -  Bangalore, Karnataka -  January 2014 to October 2016  Associate Consultant  Oracle -  Bangalore, Karnataka -  November 2012 to December 2013  EDUCATION  B.E in Computer Science Engineering  Adithya Institute of Technology -  Tamil Nadu  September 2008 to June 2012  https://www.indeed.com/r/Govardhana-K/b2de315d95905b68?isid=rex-download&ikw=download-top&co=IN https://www.indeed.com/r/Govardhana-K/b2de315d95905b68?isid=rex-download&ikw=download-top&co=IN   SKILLS  APEX. (Less than 1 year), Data Structures (3 years), FLEXCUBE (5 years), Oracle (5 years), Algorithms (3 years)  LINKS  https://www.linkedin.com/in/govardhana-k-61024944/  ADDITIONAL INFORMATION  Technical Proficiency:  Languages: Core Java, Go Lang, Data Structures & Algorithms, Oracle PL-SQL programming, Sales Force with APEX. Tools: RADTool, Jdeveloper, NetBeans, Eclipse, SQL developer, PL/SQL Developer, WinSCP, Putty Web Technologies: JavaScript, XML, HTML, Webservice  Operating Systems: Linux, Windows Version control system SVN & Git-Hub Databases: Oracle Middleware: Web logic, OC4J Product FLEXCUBE: Oracle FLEXCUBE Versions 10.x, 11.x and 12.x  https://www.linkedin.com/in/govardhana-k-61024944/',
 {'entities': [(1749, 1755, 'Companies worked at'),
   (1696, 1702, 'Companies worked at'),
   (1417, 1423, 'Companies worked at'),
   (1356, 1793, 'Skills'),
   (1209, 1215, 'Companies worked at'),
   (1136, 1248, 'Skills'),
   (928, 932, 'Graduation Year'),
   (858, 889, 'College Name'),
   (821, 856, 'Degree'),
   (787, 791, 'Graduation Year'),
   (744, 750, 'Companies worked at'),
   (722, 742, 'Designation'),
   (658, 664, 'Companies worked at'),
   (640, 656, 'Designation'),
   (574, 580, 'Companies worked at'),
   (555, 573, 'Designation'),
   (470, 493, 'Companies worked at'),
   (444, 469, 'Designation'),
   (308, 314, 'Companies worked at'),
   (234, 240, 'Companies worked at'),
   (175, 198, 'Companies worked at'),
   (93, 137, 'Email Address'),
   (39, 48, 'Location'),
   (13, 38, 'Designation'),
   (0, 12, 'Name')]})
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
        
Starting iteration 0
{'ner': 12608.92607980332}
Starting iteration 1
{'ner': 9611.061194380258}
Starting iteration 2
{'ner': 8152.459596144285}
Starting iteration 3
{'ner': 6109.995698726688}
Starting iteration 4
{'ner': 7605.971214963229}
Starting iteration 5
{'ner': 6327.344348674106}
Starting iteration 6
{'ner': 5119.813031184996}
Starting iteration 7
{'ner': 4666.953557213302}
Starting iteration 8
{'ner': 5830.451286785627}
Starting iteration 9
{'ner': 3663.190820545253}
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
         
        
        