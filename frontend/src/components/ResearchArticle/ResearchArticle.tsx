import React from 'react';
import styles from './ResearchArticle.module.css';

interface ResearchArticleProps {
  title: string;
  source: string;
  publication_date: string;
  authors: string;
  url: string;
}

const ResearchArticle: React.FC<ResearchArticleProps> = ({
  title,
  source,
  publication_date,
  authors,
  url,
}) => {
  return (
    <div data-cy="research-article" className={styles.researchArticle}>
      <a href={url} data-cy="title" target="_blank" rel="noopener noreferrer">
        {title}
      </a>
      <p data-cy="source">{source}</p>
      <p data-cy="publication_date">{publication_date}</p>
      <p data-cy="authors">{authors}</p>
    </div>
  );
};

export default ResearchArticle;
