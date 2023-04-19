import React, { useState, useEffect } from 'react';
import { fetchResearchArticleData } from '../../services/dataApi';
import {
  handlePageChange,
  getPageCount,
  getDisplayItems,
} from '../../utils/paginationHelper';
import Pagination from '../Pagination/Pagination';
import ResearchArticle from '../ResearchArticle/ResearchArticle';
import styles from './ResearchFeed.module.css';
import Loading from '../Loading/Loading';
import { ResearchArticleInterface } from '../../types/ResearchArticleInterface';

const ResearchFeed: React.FC = () => {
  const [articles, setArticles] = useState<ResearchArticleInterface[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [currentPage, setCurrentPage] = useState<number>(0);

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchResearchArticleData();
      setArticles(data);
      setIsLoading(false);
    };

    fetchData();
  }, []);

  const pageCount = getPageCount(articles.length);
  const displayArticles = getDisplayItems(articles, currentPage);

  return (
    <div className={styles.researchFeed} data-cy='research-feed'>
      {isLoading ? (
        <Loading />
      ) : (
        displayArticles.map((article, index) => (
          <ResearchArticle key={index} {...article} />
        ))
      )}
      <Pagination
        pageCount={pageCount}
        onPageChange={handlePageChange(setCurrentPage)}
      />
    </div>
  );
};

export default ResearchFeed;
