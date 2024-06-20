const express = require('express');
const fileUpload = require('express-fileupload');
const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');

const app = express();
const port = 3001;

app.use(fileUpload());

app.post('/parse-resume', (req, res) => {
    if (!req.files || !req.files.file) {
        return res.status(400).send('No files were uploaded.');
    }

    const resumePath = path.join(__dirname, 'uploads', req.files.file.name);
    req.files.file.mv(resumePath, (err) => {
        if (err) return res.status(500).send(err);

        const jobRequirements = req.body.jobRequirements;
        const command = `python process_resume.py "${resumePath}" "${jobRequirements}"`;

        exec(command, (error, stdout, stderr) => {
            if (error) {
                console.error(`exec error: ${error}`);
                return res.status(500).send('Failed to process resume');
            }
            res.send(`<pre>${stdout}</pre>`);
        });
    });
});

app.listen(port, () => {
    console.log(`Server started on http://localhost:${port}`);
});
