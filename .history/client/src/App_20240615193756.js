import './App.css';

import React, { useState } from 'react';

function App() {
    const [file, setFile] = useState(null);
    const [parsedResume, setParsedResume] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('/parse-resume', {
            method: 'POST',
            body: formData,
        });

        const result = await response.json();
        setParsedResume(result.parsed);
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
                    <button type="submit">Parse Resume</button>
                </form>
                {parsedResume && (
                    <div className=''>
                        <h2>Parsed Resume:</h2>
                        <pre>{JSON.stringify(parsedResume, null, 2)}</pre>
                    </div>
                )}
            </header>
        </div>
    );
}

export default App;
