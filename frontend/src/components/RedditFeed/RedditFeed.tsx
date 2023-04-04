import React, { useState, useEffect } from 'react';
import RedditPost from '../RedditPost/RedditPost';
import { useAuth0 } from '@auth0/auth0-react';

interface RedditPostData {
  title: string;
  url: string;
  created: number;
}

const RedditFeed: React.FC = () => {
  const [posts, setPosts] = useState<RedditPostData[]>([]);
  const { getAccessTokenSilently } = useAuth0();

  useEffect(() => {
    const getPosts = async () => {
      try {
        const token = await getAccessTokenSilently();
        console.log("Access token:", token);
        const response = await fetch(`${process.env.REACT_APP_API_URL}/api/reddit`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        const data = await response.json();
        setPosts(data);
      } catch (error) {
        console.log(error);
      }
    };
    getPosts();
  }, [getAccessTokenSilently]);

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
