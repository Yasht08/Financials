// src/ResultsPage.js

import React from 'react';
import './styles.css'; // Import the CSS file

function ResultsPage() {
    const results = JSON.parse(localStorage.getItem('results'));

    return (
        <div className="container">
            <h2>Analysis Results</h2>
            {results ? (
                <div className="result-container">
                    {JSON.stringify(results, null, 2)}
                </div>
            ) : (
                <p>No results to display</p>
            )}
        </div>
    );
}

export default ResultsPage;
