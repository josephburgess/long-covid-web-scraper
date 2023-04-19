import { useState, useEffect } from 'react';

export const useFetchData = <T>(
  fetchData: () => Promise<T[]>
): [T[], boolean] => {
  const [data, setData] = useState<T[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchDataAndSetState = async () => {
      const fetchedData = await fetchData();
      setData(fetchedData);
      setIsLoading(false);
    };

    fetchDataAndSetState();
  }, [fetchData]);

  return [data, isLoading];
};
