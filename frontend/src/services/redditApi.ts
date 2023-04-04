import { RedditPostData } from '../components/RedditFeed/RedditFeed';

export const fetchRedditPosts = async (): Promise<RedditPostData[]> => {
  try {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/api/reddit`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
    return [];
  }
};
