import React, { useState } from 'react';
import styles from './ResearchArticle.module.css';
import { ResearchArticleInterface } from '../../types/ResearchArticleInterface';

const ResearchArticle: React.FC<ResearchArticleInterface> = ({
  title,
  source,
  publication_date,
  authors,
  url,
  summary,
}) => {
  const [showFullSummary, setShowFullSummary] = useState(false);

  const toggleSummary = () => {
    setShowFullSummary(!showFullSummary);
  };

  return (
    <div data-cy='research-article' className={styles.researchArticle}>
      <a href={url} data-cy='title' target='_blank' rel='noopener noreferrer'>
        {title}
      </a>
      <p data-cy='source'>{source}</p>
      <p data-cy='publication_date'>{publication_date}</p>
      <p data-cy='authors'>{authors}</p>
      <p data-cy='summary' className={styles.summary}>
        {showFullSummary ? summary : summary.substring(0, 200)}
        ...
        <span className={styles.showMore} onClick={toggleSummary}>
          {showFullSummary ? 'Show Less' : 'Show More'}
        </span>
      </p>
    </div>
  );
};

export default ResearchArticle;
