import axios from 'axios';
import { ResearchArticleInterface } from '../types/ResearchArticleInterface';

export const fetchResearchArticleData = async (
  searchTerms: string[] = []
): Promise<ResearchArticleInterface[]> => {
  try {
    const response = await axios.get<ResearchArticleInterface[]>(
      `${process.env.REACT_APP_API_URL}/api/data`
    );

    if (searchTerms.length === 0) {
      return response.data;
    }

    return response.data.filter((item: ResearchArticleInterface) => {
      const titleAndAbstract = item.title + ' ' + item.abstract;
      return searchTerms.every((term) =>
        titleAndAbstract.toLowerCase().includes(term.toLowerCase())
      );
    });
  } catch (error) {
    console.error(error);
    return [];
  }
};
