import axios from 'axios';
import { NewsArticleInterface } from '../types/NewsArticleInterface';

export const fetchNewsArticles = async (): Promise<NewsArticleInterface[]> => {
  try {
    const response = await axios.get<NewsArticleInterface[]>(
      `${process.env.REACT_APP_API_URL}/api/news`
    );
    return response.data;
  } catch (error) {
    console.error(error);
    return [];
  }
};
