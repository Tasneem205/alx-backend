#!/usr/bin/env python3
""" simple pagination """
import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page function """
        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(page, int) and page > 0
        start, end = index_range(page, page_size)
        if start >= len(self.dataset()):
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ get hypermedia function """
        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(page, int) and page > 0
        retrieved_dataset = self.get_page(page, page_size)
        tot_pages = len(retrieved_dataset) / page_size
        tot_pages = math.ceil(tot_pages)
        return {
                "page_size": len(retrieved_dataset),
                "page": page,
                "data": retrieved_dataset,
                "next_page": page + 1 if page < tot_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": tot_pages
        }


def index_range(page, page_size):
    """index range function """
    return ((page - 1) * page_size, page * page_size)
