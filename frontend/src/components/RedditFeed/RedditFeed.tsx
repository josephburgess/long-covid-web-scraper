import React, { useState, useEffect } from 'react';
import RedditPost from '../RedditPost/RedditPost';
import { fetchRedditPosts } from '../../services/redditApi';
import Loading from '../Loading/Loading';
import Paginate from 'react-paginate';
import styles from './RedditFeed.module.css';

export interface RedditPostData {
  title: string;
  url: string;
  created: number;
  selftext: string;
}

const RedditFeed: React.FC = () => {
  const [posts, setPosts] = useState<RedditPostData[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [currentPage, setCurrentPage] = useState<number>(0);

  const handlePageChange = (selectedItem: { selected: number }) => {
    setCurrentPage(selectedItem.selected);
  };

  const itemsPerPage = 20;
  const pageCount = Math.ceil(posts.length / itemsPerPage);
  const displayPosts = posts.slice(currentPage * itemsPerPage, (currentPage * itemsPerPage) + itemsPerPage);


  useEffect(() => {
    const fetchData = async () => {
      const redditData = await fetchRedditPosts();
      setPosts(redditData);
      setIsLoading(false);
    };

    fetchData();
  }, []);

  return (
    <div className="reddit-feed">
      <h1 data-cy="reddit-feed-title">Reddit Feed</h1>
      <div className={styles['reddit-post-container']}>
      {isLoading ? (
        <Loading />
      ) : (
        displayPosts.map((post, index) => <RedditPost key={index} {...post} />)
      )}
      </div>
      <Paginate
        previousLabel={'previous'}
        nextLabel={'next'}
        breakLabel={'...'}
        breakClassName={'break-me'}
        pageCount={pageCount}
        marginPagesDisplayed={2}
        pageRangeDisplayed={5}
        onPageChange={handlePageChange}
        containerClassName={styles.pagination}
        activeClassName={styles.active}
        disabledClassName={styles.disabled}
      />
    </div>
  );
};

export default RedditFeed;
