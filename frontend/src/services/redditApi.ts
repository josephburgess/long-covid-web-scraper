import { RedditPostData } from '../components/RedditFeed/RedditFeed';

export const fetchRedditPosts = async (
  searchTerms: string[]
): Promise<RedditPostData[]> => {
  try {
    const response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/reddit`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ searchTerms }),
      }
    );
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
    return [];
  }
};
