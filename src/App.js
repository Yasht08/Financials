// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Change here
import UploadPage from './UploadPage';
import ResultsPage from './ResultsPage';

function App() {
    return (
        <Router>
            <Routes> {/* Change here */}
                <Route path="/" element={<UploadPage />} /> {/* Change here */}
                <Route path="/results" element={<ResultsPage />} /> {/* Change here */}
            </Routes> {/* Change here */}
        </Router>
    );
}

export default App;
