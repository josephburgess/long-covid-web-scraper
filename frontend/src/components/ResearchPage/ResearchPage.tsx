import React, { useState } from 'react';
import ResearchSidebar from '../ResearchSidebar/ResearchSidebar';
import YearPublishedGraph from '../YearPublishedGraph/YearPublishedGraph';
import ResearchFeed from '../ResearchFeed/ResearchFeed';
import styles from './ResearchPage.module.css';

const ResearchPage: React.FC = () => {
  const [selection, setSelection] = useState<string>('researchFeed');

  const handleSelection = (newSelection: string) => {
    setSelection(newSelection);
  };

  return (
    <div className={styles.container}>
      <div className={styles.main}>
        <ResearchSidebar onSelection={handleSelection} />
        <div className={styles.content}>
          {selection === 'researchFeed' && <ResearchFeed />}
          {selection === 'publicationTracker' && <YearPublishedGraph />}
        </div>
      </div>
    </div>
  );
};

export default ResearchPage;
