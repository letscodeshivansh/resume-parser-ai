import './App.css';

import React, { useState } from 'react';

function App() {
    const [resume, setResume] = useState('');
    const [parsedResume, setParsedResume] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError(null);
        setParsedResume(null);

        try {
            const response = await fetch('/parse-resume', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ resume }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            setParsedResume(result.parsed);
        } catch (err) {
            console.error('Error parsing resume:', err);
            setError('Failed to parse resume. Please try again.');
        }
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
                {error && <div style={{ color: 'red' }}>{error}</div>}
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
