import React, { useState } from 'react';
import Loading from '../Loading/Loading';
import RedditPost from '../RedditPost/RedditPost';
import SearchFilter from '../SearchFilter/SearchFilter';
import Pagination from '../Pagination/Pagination';
import { searchFilterTerms } from '../data/searchFilterTerms';
import { fetchRedditPosts } from '../../services/redditApi';
import {
  handlePageChange,
  getPageCount,
  getDisplayItems,
} from '../../utils/paginationHelper';
import { handleSearchTermsChange } from '../../utils/searchFilterHelper';
import styles from './RedditFeed.module.css';
import { useFetchData } from '../../hooks/useFetchData';

const RedditFeed: React.FC = () => {
  const [searchTerms, setSearchTerms] = useState<string[]>([]);
  const [currentPage, setCurrentPage] = useState<number>(0);
  const [posts, isLoading] = useFetchData(fetchRedditPosts, searchTerms);

  const pageCount = getPageCount(posts.length);
  const displayPosts = getDisplayItems(posts, currentPage);

  const selectedSearchTerms = searchTerms.map((term) => ({
    value: term,
    label: term,
  }));

  return (
    <div className='reddit-feed'>
      <h1 data-cy='reddit-feed-title'>Reddit Feed</h1>
      <div className={styles['search-filter-container']}>
        <SearchFilter
          onChange={handleSearchTermsChange(setSearchTerms)}
          searchTerms={searchFilterTerms}
          value={selectedSearchTerms}
        />
      </div>
      <div className={styles['reddit-post-container']}>
        {isLoading ? (
          <Loading />
        ) : (
          displayPosts.map((post, index) => (
            <RedditPost key={index} {...post} />
          ))
        )}
      </div>
      <Pagination
        pageCount={pageCount}
        onPageChange={handlePageChange(setCurrentPage)}
      />
    </div>
  );
};

export default RedditFeed;
