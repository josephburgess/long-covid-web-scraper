import { YearPublishedArticle } from '../components/YearPublishedGraph/YearPublishedGraph';
import { ResearchArticleData } from '../components/ResearchFeed/ResearchFeed';

const fetchData = async <T>(): Promise<T[]> => {
  try {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/api/data`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
    return [];
  }
};

export const fetchResearchArticleData = async (): Promise<
  ResearchArticleData[]
> => {
  return await fetchData<ResearchArticleData>();
};

export const fetchYearPublishedArticleData = async (): Promise<
  YearPublishedArticle[]
> => {
  return await fetchData<YearPublishedArticle>();
};
