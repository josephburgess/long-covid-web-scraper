import { useState, useEffect } from 'react';

export const useLoading = (isLoading: boolean) => {
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    if (!isLoading) {
      setLoading(false);
    }
  }, [isLoading]);

  return loading;
};
