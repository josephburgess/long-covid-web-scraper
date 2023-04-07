import React from 'react';
import { Button } from '@mui/material';
import styles from './ResearchSidebar.module.css';

interface ResearchSidebarProps {
  onSelection: (selection: string) => void;
}

const ResearchSidebar: React.FC<ResearchSidebarProps> = ({ onSelection }) => {
  return (
    <div className={styles.sidebar}>
      <Button onClick={() => onSelection('researchFeed')}>Research Feed</Button>
      <Button onClick={() => onSelection('publicationTracker')}>Publication Tracker</Button>
    </div>
  );
};

export default ResearchSidebar;
