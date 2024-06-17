

# Resume Parser  :space_invader:

This project is designed to parse resumes in PDF format, extract relevant information such as name, phone number, skills, and match those skills against job requirements. It utilizes Python, PDFPlumber, spaCy, and other libraries for natural language processing (NLP) and data analysis.

## Features :robot:

- Extracts name and phone number from resumes.
- Identifies skills mentioned in the resume text.
- Calculates a match percentage indicating how well the skills in the resume align with job requirements.
- Visualizes skill match percentage using bar charts.

## Installation :mechanical_arm:

### Prerequisites :point_down:

- Python 3.6 or higher
- pip (Python package installer)
- Node.js (for the backend server)

### Setting Up the Environment :writing_hand:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/resume-parser.git
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

## Usage :speaking_head:

1. Upload a resume in PDF format using the file input field.
2. Enter job requirements (e.g., skills needed) in the provided text box.
3. Click the "Parse Resume" button to analyze the resume.
4. View the parsed information and skill match percentage displayed in a table and visualized in a bar chart.

## Contributing :people_hugging:

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License :fist_right:

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
