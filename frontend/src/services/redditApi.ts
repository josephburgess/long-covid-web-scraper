import axios from 'axios';
import { RedditPostInterface } from '../types/RedditPostInterface';

export const fetchRedditPosts = async (
  searchTerms?: string[]
): Promise<RedditPostInterface[]> => {
  try {
    const response = await axios.post<RedditPostInterface[]>(
      `${process.env.REACT_APP_API_URL}/api/reddit`,
      { searchTerms }
    );
    return response.data;
  } catch (error) {
    console.error(error);
    return [];
  }
};
