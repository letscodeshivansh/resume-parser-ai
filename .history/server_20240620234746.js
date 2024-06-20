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
app.use(express.static(path.join(__dirname, 'client/build')));

app.post('/parse-resume', upload.single('file'), async (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded.');
  }

  const jobRequirements = req.body.jobRequirements;
  if (!jobRequirements) {
    return res.status(400).send('Job requirements not provided.');
  }

  const filePath = req.file.path;
  console.log(`File uploaded: ${filePath}`);

  try {
    const dataBuffer = fs.readFileSync(filePath);
    const data = await pdfParse(dataBuffer);

    const resumeText = data.text.replace(/(\r\n|\n|\r)/gm, " ");
    console.log('Received resume:', resumeText);

    const scriptPath = path.join(__dirname, 'process_resume.py');
    console.log(`Script path: ${scriptPath}`);

    exec(`python ${scriptPath} "${resumeText.replace(/"/g, '\\"')}" "${jobRequirements.replace(/"/g, '\\"')}"`, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return res.status(500).send('Failed to parse resume. Please try again.');
      }
      console.log(`stdout: ${stdout}`);
      console.error(`stderr: ${stderr}`);

      // Sending plain text response instead of JSON
      res.send(`<pre>${stdout}</pre>`);
    });
  } catch (err) {
    console.error(err);
    res.status(500).send('Failed to parse resume. Please try again.');
  }
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'client/build', 'index.html'));
});

const PORT = process.env.PORT || 6969;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
