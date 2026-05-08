import React, { useState } from 'react';
import TranscriptInput from './components/TranscriptInput';
import SummaryCard from './components/SummaryCard';
import ActionItemsTable from './components/ActionItemsTable';
import './App.css';

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);
  const [successMsg, setSuccessMsg] = useState('');

  const handleAnalyze = async (transcript) => {
    setIsLoading(true);
    setError(null);
    setResults(null);
    setSuccessMsg('');

    try {
      const response = await fetch('http://127.0.0.1:8000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ transcript }),
      });

      if (!response.ok) {
        throw new Error(`API Error: ${response.statusText}`);
      }

      const data = await response.json();
      setResults(data);
      setSuccessMsg('Tasks successfully stored in Notion');
    } catch (err) {
      setError(err.message || 'Failed to connect to the backend. Is it running?');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header>
        <h1>Meeting Scribe</h1>
        <p className="subtitle">AI-powered meeting assistant & prep coach</p>
      </header>

      <main>
        {error && <div className="error-message">{error}</div>}

        {successMsg && <div className="success-message">{successMsg}</div>}

        <TranscriptInput onAnalyze={handleAnalyze} isLoading={isLoading} />

        {isLoading && (
          <div className="loading-state">
            <div className="spinner"></div>
            <p>Analyzing meeting...</p>
          </div>
        )}

        {results && !isLoading && (
          <div className="results-section">
            <SummaryCard summary={results.summary} />
            <ActionItemsTable actionItems={results.action_items} />
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
