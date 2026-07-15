import './App.css';
import { useState } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [result, setResult] = useState('');

  const handlePredict = async () => {
    if (message.trim() === '') {
      setResult('Please enter a message.');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message })
      });

      const data = await response.json();

      if (data.prediction === "spam") {
        setResult("🚨 Spam Message");
      } else {
        setResult("✅ Genuine Message");
      }

    } catch (error) {
      console.error('Error:', error);
      setResult('Error connecting to backend.');
    }
  };

  return (
    <div className="app">
      <div className="card">
        <h1>📧 Spam Email Detector</h1>
        <p>Enter a message to check whether it is spam or not.</p>

        <textarea
          placeholder="Type your email/message here..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />

        <button onClick={handlePredict}>Predict</button>

        {result && <div className="result">{result}</div>}
      </div>
    </div>
  );
}

export default App;