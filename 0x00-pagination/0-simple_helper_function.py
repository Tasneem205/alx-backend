#!/usr/bin/env python3
"""Index range function file"""


def index_range(page, page_size):
    """index range function """
    return ((page - 1) * page_size, page * page_size)
