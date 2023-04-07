import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RedditFeed from './components/RedditFeed/RedditFeed';
import NewsFeed from './components/NewsFeed/NewsFeed';
import { Container, Box } from '@mui/material';
import Navbar from './components/Navbar/Navbar';
import ResearchPage from './components/ResearchPage/ResearchPage';

const App: React.FC = () => {
  return (
    <Router>
      <div>
        <Navbar />
        <Container>
          <Box sx={{ marginTop: 4 }}>
            <Routes>
              <Route path="/" element={<NewsFeed />} />
              <Route path="/research" element={<ResearchPage />} />
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
