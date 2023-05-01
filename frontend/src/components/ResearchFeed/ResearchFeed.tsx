import React, { useState, useEffect } from 'react';
import { fetchResearchArticleData } from '../../services/dataApi';
import {
  handlePageChange,
  getPageCount,
  getDisplayItems,
} from '../../utils/paginationHelper';
import Pagination from '../Pagination/Pagination';
import SearchFilter from '../SearchFilter/SearchFilter';
import { handleSearchTermsChange } from '../../utils/searchFilterHelper';
import ResearchArticle from '../ResearchArticle/ResearchArticle';
import styles from './ResearchFeed.module.css';
import Loading from '../Loading/Loading';
import { searchFilterTerms } from '../data/searchFilterTerms';
import { useFetchData } from '../../hooks/useFetchData';

interface ResearchFeedProps {
  searchFilter: string;
}

const ResearchFeed: React.FC<ResearchFeedProps> = ({ searchFilter }) => {
  const [currentPage, setCurrentPage] = useState<number>(0);
  const [searchTerms, setSearchTerms] = useState<string[]>([]);
  const [articles, isLoading] = useFetchData(
    fetchResearchArticleData,
    searchTerms
  );

  const pageCount = getPageCount(articles.length);
  const displayArticles = getDisplayItems(articles, currentPage);

  useEffect(() => {
    if (searchFilter) {
      setSearchTerms((prevSearchTerms) => {
        const newSearchTerms = new Set(prevSearchTerms);
        newSearchTerms.add(searchFilter);
        return Array.from(newSearchTerms);
      });
    }
  }, [searchFilter]);

  const selectedSearchTerms = searchTerms.map((term) => ({
    value: term,
    label: term,
  }));

  return (
    <div className={styles.researchFeed} data-cy='research-feed'>
      <div className={styles['search-filter-container']}>
        <SearchFilter
          onChange={handleSearchTermsChange(setSearchTerms)}
          searchTerms={searchFilterTerms}
          value={selectedSearchTerms}

        />
      </div>

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
