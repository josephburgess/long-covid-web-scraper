import React from 'react';
import { fetchResearchArticleData } from '../../services/dataApi';
import Pagination from '../Pagination/Pagination';
import ResearchArticle from '../ResearchArticle/ResearchArticle';
import styles from './ResearchFeed.module.css';
import Loading from '../Loading/Loading';
import { ResearchArticleInterface } from '../../types/ResearchArticleInterface';
import { useFetchData } from '../../hooks/useFetchData';
import { usePagination } from '../../hooks/usePagination';
import { useLoading } from '../../hooks/useLoading';

const ResearchFeed: React.FC = () => {
  const itemsPerPage = 20;
  const [articles, isLoading] = useFetchData<ResearchArticleInterface>(
    fetchResearchArticleData
  );

  const { setCurrentPage, pageCount, displayItems } = usePagination(
    articles,
    itemsPerPage
  );
  const loading = useLoading(isLoading);

  return (
    <div className={styles.researchFeed} data-cy='research-feed'>
      {loading ? (
        <Loading />
      ) : (
        displayItems.map((article, index) => (
          <ResearchArticle key={index} {...article} />
        ))
      )}
      <Pagination
        pageCount={pageCount}
        onPageChange={(selectedItem) => setCurrentPage(selectedItem.selected)}
      />
    </div>
  );
};

export default ResearchFeed;
