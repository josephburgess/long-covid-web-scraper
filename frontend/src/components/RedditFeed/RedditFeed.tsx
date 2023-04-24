import React from 'react';
import RedditPost from '../RedditPost/RedditPost';
import { fetchRedditPosts } from '../../services/redditApi';
import styles from './RedditFeed.module.css';
import Feed from '../Feed/Feed';

const RedditFeed: React.FC = () => (
  <div className={styles.feed}>
    <Feed
      title='Reddit Feed'
      fetchData={fetchRedditPosts}
      ItemComponent={RedditPost}
      className={styles.redditFeed}
    />
  </div>
);

export default RedditFeed;
