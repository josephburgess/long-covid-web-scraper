import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DataVisualisation from './components/DataVisualisation/DataVisualisation';
import RedditFeed from './components/RedditFeed/RedditFeed';
import NewsFeed from './components/NewsFeed/NewsFeed';
import { Container, Box } from '@mui/material';
import Navbar from './components/Navbar/Navbar';
import { Auth0Provider } from '@auth0/auth0-react';

const App: React.FC = () => {
  return (
    <Auth0Provider
      domain={process.env.REACT_APP_AUTH0_DOMAIN!}
      clientId={process.env.REACT_APP_AUTH0_CLIENT_ID!}
      authorizationParams={{ redirect_uri: window.location.origin }}
    >
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
    </Auth0Provider>
  );
}

export default App;
