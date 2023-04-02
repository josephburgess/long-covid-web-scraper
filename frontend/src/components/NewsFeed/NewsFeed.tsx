import React, { useState, useEffect } from 'react';

interface NewsArticle {
  weburl: string;
  headline: string;
  thumbnail: string;
  standfirst: string;
}

const NewsFeed: React.FC = () => {
  const [articles, setArticles] = useState<NewsArticle[]>([]);

  useEffect(() => {
    fetch('/api/news')
      .then((response) => response.json())
      .then((data) => {
        const newsData = data.map((article: any) => {
          return {
            weburl: article.weburl,
            headline: article.headline,
            thumbnail: article.thumbnail,
            standfirst: article.standfirst
          };
        });
        setArticles(newsData);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>News Feed</h1>
      <ul>
        {articles.map((article, index) => (
          <li key={index}>
            <a href={article.weburl}>{article.headline}</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NewsFeed;
