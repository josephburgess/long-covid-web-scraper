import NewsArticle from '../NewsArticle/NewsArticle';
import Loading from '../Loading/Loading';
import styles from './NewsFeed.module.css';
import { fetchNewsArticles } from '../../services/newsApi';
import { NewsArticleInterface } from '../../types/NewsArticleInterface';
import { useFetchData } from '../../hooks/useFetchData';

const NewsFeed: React.FC = () => {
  const [articles, isLoading] =
    useFetchData<NewsArticleInterface>(fetchNewsArticles);

  return (
    <div className={styles.container}>
      <h1>News Feed</h1>
      {isLoading ? (
        <Loading />
      ) : (
        <div className={styles.grid}>
          {articles.map((article, index) => (
            <NewsArticle key={index} {...article} />
          ))}
        </div>
      )}
    </div>
  );
};

export default NewsFeed;
