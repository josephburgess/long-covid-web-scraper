import { useState } from 'react';
import { getDisplayItems, getPageCount } from '../utils/paginationHelper';

export const usePagination = (items: any[], itemsPerPage: number) => {
  const [currentPage, setCurrentPage] = useState<number>(0);

  const pageCount = getPageCount(items.length, itemsPerPage);
  const displayItems = getDisplayItems(items, currentPage, itemsPerPage);

  return {
    setCurrentPage,
    pageCount,
    displayItems,
  };
};
