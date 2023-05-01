import { MultiValue, ActionMeta } from 'react-select';
import { SearchFilterItem } from './SearchFilterItem';

export interface SearchFilterProps {
  onChange: (
    selected: MultiValue<SearchFilterItem>,
    actionMeta: ActionMeta<SearchFilterItem>
  ) => void;
  searchTerms: Array<SearchFilterItem>;
  value?: SearchFilterItem[] | null;
}
