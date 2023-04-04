import { YearPublishedArticle } from '../components/YearPublishedGraph/YearPublishedGraph';

export const fetchYearPublishedArticleData = async (): Promise<
  YearPublishedArticle[]
> => {
  try {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/api/data`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
    return [];
  }
};
