const express = require('express');
const bodyParser = require('body-parser');
const multer = require('multer');
const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(bodyParser.json());

// Serve static files from the React app
app.use(express.static(path.join(__dirname, 'client/build')));

app.post('/parse-resume', upload.single('file'), (req, res) => {
    const filePath = req.file.path;
    console.log('Received file:', filePath);

    // Construct the command to run the Python script
    const scriptPath = path.join(__dirname, 'process_resume.py');
    const command = `python "${scriptPath}" "${filePath}"`;

    console.log('Executing command:', command);

    exec(command, (error, stdout, stderr) => {
        fs.unlinkSync(filePath); // Clean up the uploaded file

        if (error) {
            console.error(`exec error: ${error}`);
            return res.status(500).json({ error: 'Internal Server Error' });
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
        }

        console.log('stdout:', stdout);
        console.log('stderr:', stderr);

        try {
            const parsedResult = JSON.parse(stdout);
            res.json({ parsed: parsedResult });
        } catch (parseError) {
            console.error(`parse error: ${parseError}`);
            res.status(500).json({ error: 'Error parsing result' });
        }
    });
});

// Handle React routing, return all requests to the React app
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'client/build', 'index.html'));
});

app.listen(3000, () => {
    console.log(`Server running on port ${3000}`);
});
