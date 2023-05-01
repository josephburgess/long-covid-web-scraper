import React, { useState } from 'react';
import ResearchSidebar from '../ResearchSidebar/ResearchSidebar';
import YearPublishedGraph from '../YearPublishedGraph/YearPublishedGraph';
import WordCloud from '../WordCloud/WordCloud';
import ResearchFeed from '../ResearchFeed/ResearchFeed';
import styles from './ResearchPage.module.css';

const ResearchPage: React.FC = () => {
  const [selection, setSelection] = useState<string>('researchFeed');
  const [searchFilter, setSearchFilter] = useState<string>('');

  const handleSelection = (newSelection: string) => {
    setSelection(newSelection);
  };

  const handleWordClick = (word: string) => {
    setSearchFilter(word);
    setSelection('researchFeed');
  };

  return (
    <div className={styles.container}>
      <h1>Research</h1>
      <div className={styles.main}>
        <ResearchSidebar onSelection={handleSelection} />
        <div className={styles.content}>
          {selection === 'wordCloud' && (
            <WordCloud onWordClick={handleWordClick} />
          )}
          {selection === 'researchFeed' && (
            <ResearchFeed searchFilter={searchFilter} />
          )}
          {selection === 'publicationTracker' && <YearPublishedGraph />}
        </div>
      </div>
    </div>
  );
};

export default ResearchPage;
