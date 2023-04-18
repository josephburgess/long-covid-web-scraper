import React, { useState, useEffect } from 'react';
import { fetchResearchArticleData } from '../../services/dataApi';
import ResearchArticle from '../ResearchArticle/ResearchArticle';
import styles from './ResearchFeed.module.css';
import Loading from '../Loading/Loading';

export interface ResearchArticleData {
  title:string;
  source: string;
  publication_date: string;
  authors: string;
  url: string;
}

const ResearchFeed: React.FC = () => {
  const [articles, setArticles] = useState<ResearchArticleData[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchResearchArticleData();
      setArticles(data);
      setIsLoading(false);
    };
    
    fetchData();
  }, []);

  return (
    <div className={styles.researchFeed} data-cy="research-feed">
      {isLoading ? (
        <Loading />
      ) : (
      articles.map((article, index) => <ResearchArticle key={index} {...article} />)
      )}
    </div>
  );
};

export default ResearchFeed;

