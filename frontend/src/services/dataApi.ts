import { ResearchArticleInterface } from '../types/ResearchArticleInterface';

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
  ResearchArticleInterface[]
> => {
  return await fetchData<ResearchArticleInterface>();
};
