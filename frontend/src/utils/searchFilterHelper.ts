import { MultiValue, ActionMeta } from 'react-select';
import { SearchFilterItem } from '../types/SearchFilterItem';

export const handleSearchTermsChange =
  (setSearchTerms: (searchTerms: string[]) => void) =>
  (
    selected: MultiValue<SearchFilterItem>,
    _actionMeta: ActionMeta<SearchFilterItem>
  ) => {
    if (Array.isArray(selected)) {
      setSearchTerms(selected.map((item: SearchFilterItem) => item.value));
    } else {
      setSearchTerms([]);
    }
  };
