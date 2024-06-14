import './App.css';

import React, { useState } from 'react';

function App() {
    const [resume, setResume] = useState('');
    const [parsedResume, setParsedResume] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch('/parse-resume', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ resume }),
        });
        const result = await response.json();
        setParsedResume(result.parsed);
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Resume Parser</h1>
                <form onSubmit={handleSubmit}>
                    <textarea
                        value={resume}
                        onChange={(e) => setResume(e.target.value)}
                        placeholder="Paste your resume here"
                        rows="10"
                        cols="50"
                    ></textarea>
                    <br />
                    <button type="submit">Parse Resume</button>
                </form>
                {parsedResume && (
                    <div>
                        <h2>Parsed Resume:</h2>
                        <pre>{JSON.stringify(parsedResume, null, 2)}</pre>
                    </div>
                )}
            </header>
        </div>
    );
}

export default App;
