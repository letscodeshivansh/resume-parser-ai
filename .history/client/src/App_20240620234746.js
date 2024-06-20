import './App.css';
import React, { useState } from 'react';

function App() {
    const [file, setFile] = useState(null);
    const [jobRequirements, setJobRequirements] = useState('');
    const [parsedResume, setParsedResume] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', file);
        formData.append('jobRequirements', jobRequirements);

        const response = await fetch('/parse-resume', {
            method: 'POST',
            body: formData,
        });

        const result = await response.text();
        setParsedResume(result);
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Resume Parser</h1>
                <form onSubmit={handleSubmit}>
                    <input
                        type="file"
                        accept="application/pdf"
                        onChange={(e) => setFile(e.target.files[0])}
                    />
                    <br />
                    <textarea
                        placeholder="Enter job requirements"
                        value={jobRequirements}
                        onChange={(e) => setJobRequirements(e.target.value)}
                    />
                    <br />
                    <button type="submit">Parse Resume</button>
                </form>
                {parsedResume && (
                    <div>
                        <h2>Parsed Resume:</h2>
                        <pre>{parsedResume}</pre>
                    </div>
                )}
            </header>
        </div>
    );
}

export default App;
