import axios from 'axios';
import { WordCloudItem } from '../types/WordCloudItem';

export const fetchWordCloudData = async (): Promise<WordCloudItem[]> => {
  try {
    const response = await axios.get<WordCloudItem[]>('/api/wordcloud');
    return response.data;
  } catch (error) {
    console.error('Error fetching wordcloud data:', error);
    return [];
  }
};
