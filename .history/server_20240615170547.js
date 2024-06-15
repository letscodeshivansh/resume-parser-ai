const express = require('express');
const bodyParser = require('body-parser');
const multer = require('multer');
const pdfParse = require('pdf-parse');
const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'clientbuild')));

app.post('/parse-resume', upload.single('file'), async (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded.');
  }

  const filePath = req.file.path;
  try {
    const dataBuffer = require('fs').readFileSync(filePath);
    const data = await pdfParse(dataBuffer);

    const resumeText = data.text.replace(/(\r\n|\n|\r)/gm, " ");
    console.log('Received resume:', resumeText);

    exec(`python ${path.join(__dirname, 'process_resume.py')} "${resumeText}"`, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return res.status(500).send('Failed to parse resume. Please try again.');
      }
      console.log(`stdout: ${stdout}`);
      console.error(`stderr: ${stderr}`);

      res.json({ parsed: stdout });
    });
  } catch (err) {
    console.error(err);
    res.status(500).send('Failed to parse resume. Please try again.');
  }
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../client/build', 'index.html'));
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
