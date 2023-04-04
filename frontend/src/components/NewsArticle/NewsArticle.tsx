import React from 'react';
import styles from './NewsArticle.module.css';

interface NewsArticleProps {
  webUrl: string;
  headline: string;
  thumbnail: string;
  standfirst: string;
  date: string;
}

const NewsArticle: React.FC<NewsArticleProps> = ({ webUrl, headline, thumbnail, standfirst, date }) => {
  return (
    <div className={styles.articleContainer}>
      <a href={webUrl} data-cy="webUrl" className={styles.articleLink}>
        <div className={styles.thumbnail}>
          <img src={thumbnail} alt={headline} data-cy="thumbnail" />
        </div>
        <h2 className={styles.headline} data-cy="headline">{headline}</h2>
        <p className={styles.date} data-cy="date">{date}</p>
        <p className={styles.standfirst} data-cy="standfirst">{standfirst}</p>
      </a>
    </div>
  );
};

export default NewsArticle;
