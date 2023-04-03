import React from 'react';
import { formatDistanceToNowStrict } from 'date-fns';
import styles from './RedditPost.module.css';

interface RedditPostProps {
  title: string;
  url: string;
  created: number;
}

const RedditPost: React.FC<RedditPostProps> = ({ title, url, created }) => {
  const timestampText = formatDistanceToNowStrict(new Date(created * 1000), { addSuffix: true });

  return (
    <div className={styles['reddit-post']}>
      <div className={styles['reddit-post-thumbnail']}>
        <img data-cy="thumbnail" src="https://www.redditstatic.com/desktop2x/img/favicon/favicon-32x32.png" alt="Reddit Thumbnail" />
      </div>
      <div className={styles['reddit-post-content']}>
        <a href={url} data-cy="title">{title}</a>
        <div data-cy="timestamp" className={styles['reddit-post-timestamp']}>{timestampText}</div>
      </div>
    </div>
  );
};

export default RedditPost;
