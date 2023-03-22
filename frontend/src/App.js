import logo from './logo.svg';
import './App.css';
import YearPublishedGraph from './components/YearPublished/YearPublished';

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
