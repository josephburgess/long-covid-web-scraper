export const handlePageChange =
  (setCurrentPage: (page: number) => void) =>
  (selectedItem: { selected: number }) => {
    setCurrentPage(selectedItem.selected);
  };

const itemsPerPage = 20;

export const getPageCount = (itemsLength: number) => {
  return Math.ceil(itemsLength / itemsPerPage);
};

export const getDisplayItems = <T extends any>(
  items: T[],
  currentPage: number
) => {
  return items.slice(
    currentPage * itemsPerPage,
    currentPage * itemsPerPage + itemsPerPage
  );
};
