// server.js
const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');
const app = express();

app.use(bodyParser.json());

app.post('/parse-resume', (req, res) => {
    const resume = req.body.resume;

    // Command to run the Python script
    const command = `python main.py "${resume}"`;

    exec(command, (error, stdout, stderr) => {
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
