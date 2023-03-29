import React, { useState, useEffect } from 'react';

interface RedditPost {
  title: string;
  url: string;
}

const RedditFeed: React.FC = () => {
  const [posts, setPosts] = useState<RedditPost[]>([]);

  useEffect(() => {
    // Fetch data from Reddit API
    fetch('https://www.reddit.com/r/longhaulers.json')
      .then((response) => response.json())
      .then((data) => {
        const postsData = data.data.children.map((post: any) => {
          return {
            title: post.data.title,
            url: post.data.url,
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
