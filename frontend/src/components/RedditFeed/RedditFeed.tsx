import React, { useState, useEffect } from 'react';
import RedditPost from '../RedditPost/RedditPost';
import { fetchRedditPosts } from '../../services/redditApi';

export interface RedditPostData {
  title: string;
  url: string;
  created: number;
}

const RedditFeed: React.FC = () => {
  const [posts, setPosts] = useState<RedditPostData[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const redditData = await fetchRedditPosts();
      setPosts(redditData);
    };

    fetchData();
  }, []);

  return (
    <div className="reddit-feed">
      <h1>Reddit Feed</h1>
      {posts.map((post, index) => (
        <RedditPost key={index} {...post} />
      ))}
    </div>
  );
};

export default RedditFeed;
