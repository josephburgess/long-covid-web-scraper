import React, { useState, useEffect } from 'react';

interface RedditPost {
  title: string;
  url: string;
}

const RedditFeed: React.FC = () => {
  const [posts, setPosts] = useState<RedditPost[]>([]);

  useEffect(() => {
    fetch('/api/reddit')
      .then((response) => response.json())
      .then((data) => {
        const postsData = data.map((post: any) => {
          return {
            title: post.title,
            url: post.url,
          };
        });
        setPosts(postsData);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Reddit Feed</h1>
      <ul>
        {posts.map((post, index) => (
          <li key={index}>
            <a href={post.url}>{post.title}</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RedditFeed;
