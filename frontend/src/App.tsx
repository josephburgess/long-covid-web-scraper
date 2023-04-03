import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DataVisualisation from './components/DataVisualisation/DataVisualisation';
import RedditFeed from './components/RedditFeed/RedditFeed';
import NewsFeed from './components/NewsFeed/NewsFeed';
import { Container, Box } from '@mui/material';
import Navbar from './components/Navbar/Navbar';

const App: React.FC = () => {
  return (
    <Router>
      <div>
        <Navbar />
        <Container>
          <Box sx={{ marginTop: 4 }}>
            <Routes>
              <Route path="/" element={<NewsFeed />} />
              <Route path="/research" element={<DataVisualisation />} />
              <Route path="/reddit" element={<RedditFeed />} />
              <Route path="/news" element={<NewsFeed />} />
            </Routes>
          </Box>
        </Container>
      </div>
    </Router>
  );
}

export default App;
