#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)


class Server():
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Paginates the dataset correctly and returns the appropriate page
        of the dataset (i.e. the correct list of rows).
        """
        try:
            assert type(page) is int
            assert type(page_size) is int
            assert page > 0
            assert page_size > 0
            slicelist = index_range(page, page_size)
            start = slicelist[0]
            end = slicelist[1]
            try:
                return self.dataset()[start:end]
            except IndexError:
                return []

        except AssertionError:
            return
