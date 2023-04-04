import { NewsArticleData } from '../components/NewsFeed/NewsFeed';

export const fetchNewsArticles = async (): Promise<NewsArticleData[]> => {
  try {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/api/news`);
    const data = await response.json();
    return data.map((article: NewsArticleData) => ({
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
