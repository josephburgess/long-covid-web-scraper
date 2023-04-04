// NewsFeed.tsx
import React, { useState, useEffect } from 'react';
import NewsArticle from '../NewsArticle/NewsArticle';
import styles from './NewsFeed.module.css';

interface NewsArticleData {
  weburl: string;
  headline: string;
  thumbnail: string;
  standfirst: string;
  date: string;
}

const NewsFeed: React.FC = () => {
  const [articles, setArticles] = useState<NewsArticleData[]>([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/api/news`)
      .then((response) => response.json())
      .then((data) => {
        const newsData = data.map((article: NewsArticleData) => {
          return {
            weburl: article.weburl,
            headline: article.headline,
            thumbnail: article.thumbnail,
            standfirst: article.standfirst,
            date: article.date,
          };
        });
        setArticles(newsData);
      })
      .catch((error) => {
        console.log(error);
      });
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
