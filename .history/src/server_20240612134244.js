const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const path = require("path");
const http = require("http");

require("dotenv").config();
const server = http.createServer(app);


app.use(bodyParser.json());

app.post('/parse-resume', (req, res) => {
    const resume = req.body.resume;npm
    // Call Python script for processing (using child_process or a similar method)
    // Return the parsed and scored resume data
    res.json({ message: 'Resume parsed successfully' });
});

app.listen(6969, () => {
    console.log('Server running on port 6969');
});
