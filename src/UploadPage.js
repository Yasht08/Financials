// src/UploadPage.js

import React, { useState } from 'react';
import axios from 'axios';
import './styles.css';  // Import the CSS file

function UploadPage() {
    const [file, setFile] = useState(null);
    const [error, setError] = useState(null);

    const handleUpload = async () => {
        if (!file) {
            setError('Please select a file first');
            return;
        }
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:5000/upload', formData);
            localStorage.setItem('results', JSON.stringify(response.data));
            window.location.href = '/results'; // Redirect to results page
        } catch (error) {
            console.error('Error uploading file:', error);
            setError('Failed to upload the file');
        }
    };

    return (
        <div className="container">
            <h2>Upload data.json</h2>
            <input 
                type="file" 
                onChange={(e) => setFile(e.target.files[0])} 
                accept=".json"
            />
            <button onClick={handleUpload}>Submit</button>
            {error && <p className="error">{error}</p>} {/* Display error message */}
        </div>
    );
}

export default UploadPage;
