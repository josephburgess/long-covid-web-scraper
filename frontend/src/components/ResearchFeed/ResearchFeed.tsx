import React from 'react';
import { fetchResearchArticleData } from '../../services/dataApi';
import ResearchArticle from '../ResearchArticle/ResearchArticle';
import styles from './ResearchFeed.module.css';
import Feed from '../Feed/Feed';

const ResearchFeed: React.FC = () => (
  <Feed
    title='Research Feed'
    fetchData={fetchResearchArticleData}
    ItemComponent={ResearchArticle}
    className={styles.researchFeed}
  />
);

export default ResearchFeed;
