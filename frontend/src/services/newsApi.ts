import { NewsArticleInterface } from '../types/NewsArticleInterface';

export const fetchNewsArticles = async (): Promise<NewsArticleInterface[]> => {
  try {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/api/news`);
    const data = await response.json();
    return data.map((article: NewsArticleInterface) => ({
      webUrl: article.webUrl,
      headline: article.headline,
      thumbnail: article.thumbnail,
      standfirst: article.standfirst,
      date: article.date,
    }));
  } catch (error) {
    console.error(error);
    return [];
  }
};
