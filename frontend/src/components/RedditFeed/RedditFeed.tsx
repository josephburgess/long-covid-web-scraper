import React, { useState, useEffect } from 'react';
import RedditPost from '../RedditPost/RedditPost';

interface RedditPostData {
  title: string;
  url: string;
  created: number;
}

const RedditFeed: React.FC = () => {
  const [posts, setPosts] = useState<RedditPostData[]>([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/api/reddit`)
      .then((response) => response.json())
      .then((data) => {
        setPosts(data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className="reddit-feed">
      <h1>Reddit Feed</h1>
      {posts.map((post: RedditPostData, index) => (
        <RedditPost key={index} title={post.title} url={post.url} created={post.created} />
      ))}
    </div>
  );
};

export default RedditFeed;
