import { useState, useEffect } from 'react';

export const useFetchData = <T>(
  fetchDataFunction: (searchTerms?: string[]) => Promise<T[]>,
  searchTerms?: string[]
): [T[], boolean] => {
  const [data, setData] = useState<T[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      const fetchedData = await fetchDataFunction(searchTerms);
      setData(fetchedData);
      setIsLoading(false);
    };

    fetchData();
  }, [fetchDataFunction, searchTerms]);

  return [data, isLoading];
};
