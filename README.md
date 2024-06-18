


# Resume Parser  :space_invader:




This project is designed to parse resumes in PDF format, extract relevant information such as name, phone number, skills, and match those skills against job requirements. It utilizes Python, PDFPlumber, spaCy, and other libraries for natural language processing (NLP) and data analysis.

## Features 📔

- Extracts name and phone number from resumes.
- Identifies skills mentioned in the resume text.
- Calculates a match percentage indicating how well the skills in the resume align with job requirements.
- Visualizes skill match percentage using bar charts.

## TeckStack 🤖

<br>
<div align="center">
	<code><img width="55" src="https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png" alt="JavaScript" title="JavaScript"/></code>
	<code><img width="55" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/></code>
	<code><img width="55" src="https://user-images.githubusercontent.com/25181517/183897015-94a058a6-b86e-4e42-a37f-bf92061753e5.png" alt="React" title="React"/></code>
	<code><img width="55" src="https://user-images.githubusercontent.com/25181517/183568594-85e280a7-0d7e-4d1a-9028-c8c2209e073c.png" alt="Node.js" title="Node.js"/></code>
	<code><img width="55" src="https://user-images.githubusercontent.com/25181517/183859966-a3462d8d-1bc7-4880-b353-e2cbed900ed6.png" alt="Express" title="Express"/></code>
	<code><img width="55" src="https://user-images.githubusercontent.com/25181517/192108891-d86b6220-e232-423a-bf5f-90903e6887c3.png" alt="Visual Studio Code" title="Visual Studio Code"/></code>
</div>
<br>

## Installation :mechanical_arm:

### Prerequisites :point_down:

- Python 3.6 or higher
- pip (Python package installer)
- Node.js (for the backend server)

### Setting Up the Environment :writing_hand:

1. Clone the repository:

   ```bash
   git clone https://github.com/letscodeshivansh/resume-parser-ai.git
   cd resume-parser
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   .\env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install Node.js dependencies:
   ```bash
   cd client
   npm install
   ```
### Running the Application: :mechanical_leg:

1. Start the backend server (Node.js):

   ```bash
   npm start

   ```
2. In another terminal, start the frontend development server (React)::
   ```bash
   cd client
   npm start

   ```
3. Open your web browser and navigate to http://localhost:6969 to access the application

## Usage 🚶

1. Upload a resume in PDF format using the file input field.
2. Enter job requirements (e.g., skills needed) in the provided text box.
3. Click the "Parse Resume" button to analyze the resume.
4. View the parsed information and skill match percentage displayed in a table and visualized in a bar chart.

## Contributing :people_hugging:

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License 👮

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments :brain:

- **PDFPlumber**: For extracting text from PDF resumes.
- **spaCy**: For natural language processing capabilities.
- **React**: For building the user interface.
- **Node.js / Express**: For the backend server.
- **Matplotlib / Seaborn**: For data visualization.
- **FuzzyWuzzy**: For fuzzy string matching.

## Screenshots :v:
![image](https://github.com/letscodeshivansh/resume-parser-ai/assets/125864444/ad2b8483-cede-4293-890d-479cfebedf09)
