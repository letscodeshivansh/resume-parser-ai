const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const path = require("path");
const http = require("http")

require("dotenv".config())


app.use(bodyParser.json());

app.post('/parse-resume', (req, res) => {
    const resume = req.body.resume;
    // Call Python script for processing (using child_process or a similar method)
    // Return the parsed and scored resume data
    res.json({ message: 'Resume parsed successfully' });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
