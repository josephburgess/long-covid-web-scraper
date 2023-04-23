import React, { useState, useEffect } from 'react';
import Loading from '../Loading/Loading';
import RedditPost from '../RedditPost/RedditPost';
import SearchFilter from '../SearchFilter/SearchFilter';
import Pagination from '../Pagination/Pagination';
import { redditSearchTerms } from '../data/redditSearchTerms';
import { RedditPostInterface } from '../../types/RedditPostInterface';
import { useFetchData } from '../../hooks/useFetchData';
import { usePagination } from '../../hooks/usePagination';
import { useLoading } from '../../hooks/useLoading';
import { fetchFilteredRedditPosts } from '../../utils/redditHelper';
import { handleSearchTermsChange } from '../../utils/searchFilterHelper';
import styles from './RedditFeed.module.css';

const RedditFeed: React.FC = () => {
  const itemsPerPage = 20;
  const [searchTerms, setSearchTerms] = useState<string[]>([]);

  const fetchPosts = fetchFilteredRedditPosts(searchTerms);
  const [posts, isLoading] = useFetchData<RedditPostInterface>(fetchPosts);

  useEffect(() => {
    setSearchTerms([]);
  }, []);

  const { setCurrentPage, pageCount, displayItems } = usePagination(
    posts,
    itemsPerPage
  );
  const loading = useLoading(isLoading);

  return (
    <div className='reddit-feed'>
      <h1 data-cy='reddit-feed-title'>Reddit Feed</h1>
      <div className={styles['search-filter-container']}>
        <SearchFilter
          onChange={handleSearchTermsChange(setSearchTerms)}
          searchTerms={redditSearchTerms}
        />
      </div>
      <div className={styles['reddit-post-container']}>
        {loading ? (
          <Loading />
        ) : (
          displayItems.map((post, index) => (
            <RedditPost key={index} {...post} />
          ))
        )}
      </div>
      <Pagination
        pageCount={pageCount}
        onPageChange={(selectedItem) => setCurrentPage(selectedItem.selected)}
      />
    </div>
  );
};

export default RedditFeed;
