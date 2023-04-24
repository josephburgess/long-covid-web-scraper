import { ResearchArticleInterface } from '../types/ResearchArticleInterface';

const fetchData = async <T>(searchTerms: string[] = []): Promise<T[]> => {
  try {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/api/data`);
    const data = await response.json();

    if (searchTerms.length === 0) {
      return data;
    }

    const filteredData = data.filter((item: ResearchArticleInterface) => {
      const titleAndAbstract = item.title + ' ' + item.abstract;
      return searchTerms.every((term) =>
        titleAndAbstract.toLowerCase().includes(term.toLowerCase())
      );
    });

    return filteredData;
  } catch (error) {
    console.error(error);
    return [];
  }
};

export const fetchResearchArticleData = async (
  searchTerms: string[] = []
): Promise<ResearchArticleInterface[]> => {
  return await fetchData<ResearchArticleInterface>(searchTerms);
};
