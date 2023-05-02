import { WordCloudItem } from '../types/WordCloudItem';

interface WordClickCallbacks {
  onWordClick: (word: WordCloudItem) => void;
}

export const useWordClickCallbacks = (
  onWordClick: (word: string) => void
): WordClickCallbacks => {
  return {
    onWordClick: (word: WordCloudItem) => {
      onWordClick(word.text);
    },
  };
};
