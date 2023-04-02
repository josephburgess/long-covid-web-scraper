import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import NewsArticles from './components/NewsArticles/NewsArticles';
import DataVisualisation from './components/DataVisualisation/DataVisualisation';
import RedditFeed from './components/RedditFeed/RedditFeed';
import NewsFeed from './components/NewsFeed/NewsFeed';
import { AppBar, Toolbar, Typography, Button, Container, Box } from '@mui/material';

function App() {
  return (
    <Router>
      <div>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Long COVID News Hub
            </Typography>
            <Button color="inherit" component={Link} to="/news">
              News Articles
            </Button>
            <Button color="inherit" component={Link} to="/data-visualization">
              Data
            </Button>
            <Button color="inherit" component={Link} to="/reddit-feed">
              Reddit Feed
            </Button>
          </Toolbar>
        </AppBar>
        <Container>
          <Box sx={{ marginTop: 4 }}>
            <Routes>
              <Route path="/" element={<NewsArticles />} />
              <Route path="/data-visualization" element={<DataVisualisation />} />
              <Route path="/reddit-feed" element={<RedditFeed />} />
              <Route path="/news" element={<NewsFeed />} />
            </Routes>
          </Box>
        </Container>
      </div>
    </Router>
  );
}

export default App;
