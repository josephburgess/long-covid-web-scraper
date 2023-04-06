import React, { useState, useEffect } from 'react';
import RedditPost from '../RedditPost/RedditPost';
import { fetchRedditPosts } from '../../services/redditApi';
import Loading from '../Loading/Loading';

export interface RedditPostData {
  title: string;
  url: string;
  created: number;
}

const RedditFeed: React.FC = () => {
  const [posts, setPosts] = useState<RedditPostData[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);

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
      <h1>Reddit Feed</h1>
      {isLoading ? (
        <Loading />
      ) : (
        posts.map((post, index) => <RedditPost key={index} {...post} />)
      )}
    </div>
  );
};

export default RedditFeed;
