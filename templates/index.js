import React, { useState } from 'react';

import axios from 'axios';

function ResumeUpload() {
    const [file, setFile] = useState(null);
    const [result, setResult] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('resume', file);
        const response = await axios.post('/parse-resume', formData);
        setResult(response.data);
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload Resume</button>
            {result && <div>{JSON.stringify(result)}</div>}
        </div>
    );
}

export default ResumeUpload;
