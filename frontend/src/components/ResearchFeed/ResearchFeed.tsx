import React, { useState } from 'react';
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
import { useFetchData } from '../../hooks/useFetchData';

const ResearchFeed: React.FC = () => {
  const [currentPage, setCurrentPage] = useState<number>(0);

  const [articles, isLoading] = useFetchData<ResearchArticleInterface>(
    fetchResearchArticleData
  );

  const pageCount = getPageCount(articles.length);
  const displayArticles = getDisplayItems(articles, currentPage);

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
