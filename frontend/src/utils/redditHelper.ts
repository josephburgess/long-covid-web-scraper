import { fetchRedditPosts } from '../services/redditApi';

export const fetchFilteredRedditPosts = (searchTerms: string[]) => () =>
  fetchRedditPosts(searchTerms);
