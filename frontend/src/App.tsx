import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
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
              Long COVID Hub
            </Typography>
            <Button color="inherit" component={Link} to="/news">
              News
            </Button>
            <Button color="inherit" component={Link} to="/research">
              Data
            </Button>
            <Button color="inherit" component={Link} to="/reddit">
              Reddit Feed
            </Button>
          </Toolbar>
        </AppBar>
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
