import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import styles from './Navbar.module.css';
import { useAuth0, LogoutOptions } from '@auth0/auth0-react';
const Navbar: React.FC = () => {
  const { loginWithRedirect, logout, isAuthenticated } = useAuth0();

  return (
    <AppBar position="static" className={styles.appBar} data-cy="navbar">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }} className={styles.title} data-cy="navbar-title">
          Long COVID Hub
        </Typography>
        <Button color="inherit" component={Link} to="/news" className={styles.button} data-cy="navbar-link-news">
          News
        </Button>
        <Button color="inherit" component={Link} to="/research" className={styles.button} data-cy="navbar-link-data">
          Data
        </Button>
        <Button color="inherit" component={Link} to="/reddit" className={styles.button} data-cy="navbar-link-reddit">
          Reddit Feed
        </Button>
        {!isAuthenticated && (
          <Button color="inherit" onClick={() => loginWithRedirect()} className={styles.button} data-cy="navbar-link-login">
            Log in
          </Button>
        )}
        {isAuthenticated && (
        <Button color="inherit" onClick={() => logout({ returnTo: window.location.origin, federated: true } as LogoutOptions)} className={styles.button} data-cy="navbar-link-logout">
        Log out
        </Button>  
        )}
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
