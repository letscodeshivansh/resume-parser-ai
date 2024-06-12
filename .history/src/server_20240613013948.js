

const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');
const path = require('path');
const app = express();

app.use(bodyParser.json());

app.post('/parse-resume', (req, res) => {
    const resume = req.body.resume;

    const escapedResume = resume.replace(/"/g, '\\"');

    // Construct the command to run the Python script
    const scriptPath = path.join(__dirname, 'process_resume.py');
    const command = `python "${scriptPath}" "${escapedResume}"`;

    exec(command, { shell: 'cmd.exe' }, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.status(500).json({ error: 'Internal Server Error' });
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return res.status(500).json({ error: 'Internal Server Error' });
        }

        try {
            const parsedResult = JSON.parse(stdout);
            res.json({ parsed: parsedResult });
        } catch (parseError) {
            console.error(`parse error: ${parseError}`);
            res.status(500).json({ error: 'Error parsing result' });
        }
    });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
