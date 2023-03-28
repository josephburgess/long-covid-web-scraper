import React from 'react';
import YearPublishedGraph from './components/YearPublishedGraph/YearPublishedGraph';
import './App.css';

function App() {
  return (
    <div className='App'>
      <header className='App-header'>
        <h1>Long COVID Articles Visualization</h1>
      </header>
      <main>
        <YearPublishedGraph />
      </main>
    </div>
  );
}

export default App;
