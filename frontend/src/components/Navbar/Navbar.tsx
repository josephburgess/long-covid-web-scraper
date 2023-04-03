// components/Navbar.tsx
import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import styles from './Navbar.module.css';

const Navbar: React.FC = () => {
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
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
