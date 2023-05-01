import React from 'react';
import CreatableSelect from 'react-select/creatable';
import makeAnimated from 'react-select/animated';
import styles from './SearchFilter.module.css';
import { SearchFilterProps } from '../../types/SearchFilterProps';
const animatedComponents = makeAnimated();

const SearchFilter: React.FC<SearchFilterProps> = ({
  onChange,
  searchTerms,
  value,
}) => (
  <CreatableSelect
    closeMenuOnSelect={false}
    components={animatedComponents}
    isMulti
    classNamePrefix='search-filter'
    options={searchTerms}
    value={value}
    onChange={onChange}
    className={styles['search-filter']}
  />
);

export default SearchFilter;
