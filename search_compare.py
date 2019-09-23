#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assignment4_part_1"""

import random
import timeit


def sequential_search(lst, target_element):
    start = timeit.default_timer()

    idx_found = -1
    for i in range(0, len(lst)):
        if lst[i] == target_element:
            idx_found = i
            break

    stop = timeit.default_timer()
    time_takes = stop - start
    return idx_found, time_takes


def ordered_sequential_search(lst, target_element):
    start = timeit.default_timer()
    idx_found = -1
    for i in range(0, len(lst)):
        if lst[i] == target_element:
            idx_found = i
            break
        elif lst[i] > target_element:
            idx_found = -1
            break

    stop = timeit.default_timer()
    time_takes = stop - start
    return idx_found, time_takes


def binary_search_iterative(lst, target_element):
    start = timeit.default_timer()

    l = 0
    r = 99
    idx_found = -1
    while l <= r:

        mid = int(l + (r - l) / 2)

        if lst[mid] == target_element:
            idx_found = mid
            break

        elif lst[mid] < target_element:
            l = mid + 1

        else:
            r = mid - 1

    stop = timeit.default_timer()
    time_takes = stop - start
    return idx_found, time_takes


def binary_search_recursive(lst, l, r, target_element):
    """Check base case"""
    if r >= l:

        mid = int(l + (r - l) / 2)

        if lst[mid] == target_element:
            return mid

        elif lst[mid] > target_element:
            return binary_search_recursive(lst, l, mid - 1, target_element)

        else:
            return binary_search_recursive(lst, mid + 1, r, target_element)

    else:
        return -1


def main():
    lists_size = [500, 1000, 10000]

    for cur_list_size in lists_size:
        average_seq = 0
        average_ordered_seq = 0
        average_binary_search_iterative = 0
        average_binary_search_recursive = 0

        for list_number in range(100):
            lst = []
            for r in range(cur_list_size):
                cur_number = random.randint(1, 100000000)
                lst.append(cur_number)

            """sequential search"""
            result, time_takes = sequential_search(lst, -1)
            average_seq += time_takes

            """ordered_sequential"""
            lst = sorted(lst)

            result, time_takes = ordered_sequential_search(lst, -1)
            average_ordered_seq += time_takes

            result, time_takes = binary_search_iterative(lst, -1)
            average_binary_search_iterative += time_takes

            start = timeit.default_timer()
            result = binary_search_recursive(lst, -1, 0, 99)
            stop = timeit.default_timer()
            average_binary_search_recursive += (stop - start)

        average_seq /= 100.0
        average_ordered_seq /= 100.0
        average_binary_search_iterative /= 100.0
        average_binary_search_recursive /= 100.0

        print("For 100 List of size", cur_list_size)
        print("Sequential Search took %10.7f seconds to run, on average" % average_seq)
        print("Ordered Sequential Search took %10.7f seconds to run, on average" % average_ordered_seq)
        print("Binary Search Iterative  took %10.7f seconds to run, on average" % average_binary_search_iterative)
        print("Binary Search Recursive took %10.7f seconds to run, on average" % average_binary_search_recursive)
        print("")


main()
