import React, { useState } from 'react';
import Pagination from '../Pagination/Pagination';
import SearchFilter from '../SearchFilter/SearchFilter';
import {
  handlePageChange,
  getPageCount,
  getDisplayItems,
} from '../../utils/paginationHelper';
import { handleSearchTermsChange } from '../../utils/searchFilterHelper';
import Loading from '../Loading/Loading';
import { searchFilterTerms } from '../data/searchFilterTerms';
import { useFetchData } from '../../hooks/useFetchData';

interface FeedProps {
  title: string;
  fetchData: (searchTerms?: string[]) => Promise<any[]>;
  ItemComponent: React.FC<any>;
  className?: string;
}

const Feed: React.FC<FeedProps> = ({
  title,
  fetchData,
  ItemComponent,
  className,
}) => {
  const [searchTerms, setSearchTerms] = useState<string[]>([]);
  const [currentPage, setCurrentPage] = useState<number>(0);
  const [items, isLoading] = useFetchData(fetchData, searchTerms);

  const pageCount = getPageCount(items.length);
  const displayItems = getDisplayItems(items, currentPage);

  return (
    <div className={className}>
      <h1>{title}</h1>
      <div className='search-filter-container'>
        <SearchFilter
          onChange={handleSearchTermsChange(setSearchTerms)}
          searchTerms={searchFilterTerms}
        />
      </div>
      <div className='item-container'>
        {isLoading ? (
          <Loading />
        ) : (
          displayItems.map((item, index) => (
            <ItemComponent key={index} {...item} />
          ))
        )}
      </div>
      <Pagination
        pageCount={pageCount}
        onPageChange={handlePageChange(setCurrentPage)}
      />
    </div>
  );
};

export default Feed;
