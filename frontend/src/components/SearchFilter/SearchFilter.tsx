import React from 'react';
import { MultiValue, ActionMeta } from 'react-select';
import CreatableSelect from 'react-select/creatable';
import makeAnimated from 'react-select/animated';

const animatedComponents = makeAnimated();

interface SearchFilterBarProps {
  onChange: (selected: MultiValue<{ value: string; label: string }>, actionMeta: ActionMeta<{ value: string; label: string }>) => void;
  searchTerms: Array<{ value: string; label: string }>;
}

const SearchFilter: React.FC<SearchFilterBarProps> = ({ onChange, searchTerms }) => (
  <CreatableSelect
    closeMenuOnSelect={false}
    components={animatedComponents}
    isMulti
    classNamePrefix="search-filter"
    options={searchTerms}
    onChange={onChange}
  />
);

export default SearchFilter;