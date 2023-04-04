import React, { useState, useEffect } from 'react';
import NewsArticle from '../NewsArticle/NewsArticle';
import styles from './NewsFeed.module.css';
import { fetchNewsArticles } from '../../services/newsApi';

export interface NewsArticleData {
  webUrl: string;
  headline: string;
  thumbnail: string;
  standfirst: string;
  date: string;
}

const NewsFeed: React.FC = () => {
  const [articles, setArticles] = useState<NewsArticleData[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const newsData = await fetchNewsArticles();
      setArticles(newsData);
    };

    fetchData();
  }, []);

  return (
    <div className={styles.container}>
      <h1>News Feed</h1>
      <div className={styles.grid}>
        {articles.map((article, index) => (
          <NewsArticle
            key={index}
            {...article}
          />
        ))}
      </div>
    </div>
  );
};

export default NewsFeed;
