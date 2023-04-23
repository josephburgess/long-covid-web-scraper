export const handlePageChange =
  (setCurrentPage: (page: number) => void) =>
  (selectedItem: { selected: number }) =>
    setCurrentPage(selectedItem.selected);

export const getPageCount = (totalItems: number, itemsPerPage: number) => {
  return Math.ceil(totalItems / itemsPerPage);
};

export const getDisplayItems = (
  items: any[],
  currentPage: number,
  itemsPerPage: number
) => {
  const startIndex = currentPage * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;

  return items.slice(startIndex, endIndex);
};
