import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import MapSpace from './Map.js';

function App() {
  const [the_values, getValues] = useState(null);

  return (
    <div className="App">
      <header className="App-header">
        <MapSpace />
      </header>
    </div>
  );
}

export default App;
