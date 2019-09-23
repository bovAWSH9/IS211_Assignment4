#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assignment4_part_2"""

import random
import timeit


def insertion_sort(lst):
    start = timeit.default_timer()

    for idx1 in range(1, len(lst)):

        key = lst[idx1]

        idx2 = idx1 - 1
        while idx2 >= 0 and key < lst[idx2]:
            lst[idx2 + 1] = lst[idx2]
            idx2 -= 1
        lst[idx2 + 1] = key

    stop = timeit.default_timer()
    time_takes = stop - start
    return lst, time_takes


def shell_sort(lst):
    start = timeit.default_timer()
    n = len(lst)
    space = n // 2

    while space > 0:
        for idx1 in range(space, n):
            temp = lst[idx1]
            idx2 = idx1
            while idx2 >= space and lst[idx2 - space] > temp:
                lst[idx2] = lst[idx2 - space]
                idx2 -= space

            lst[idx2] = temp
        space //= 2

    stop = timeit.default_timer()
    time_takes = stop - start
    return lst, time_takes


def python_sort(lst):
    start = timeit.default_timer()
    lst = sorted(lst)

    stop = timeit.default_timer()
    time_takes = stop - start
    return lst, time_takes


def main():
    lists_size = [500, 1000, 10000]

    for cur_list_size in lists_size:
        average_insertion_sort = 0
        average_shell_sort = 0
        average_python_sort = 0

        for list_number in range(100):
            lst = []
            for r in range(cur_list_size):
                cur_number = random.randint(1, 100000000)
                lst.append(cur_number)

        """insertion_sort"""
        result, time_takes = insertion_sort(lst)
        average_insertion_sort += time_takes

        """insertion_sort"""
        result, time_takes = shell_sort(lst)
        average_shell_sort += time_takes

        """insertion_sort"""
        result, time_takes = python_sort(lst)
        average_python_sort += time_takes

        average_insertion_sort /= 100.0
        average_shell_sort /= 100.0
        average_python_sort /= 100.0

        print("For 100 List of size", cur_list_size)
        print("Insertion sort took %10.7f seconds to run, on average" % average_insertion_sort)
        print("Shell Sort took %10.7f seconds to run, on average" % average_shell_sort)
        print("Python Sort  took %10.7f seconds to run, on average" % average_python_sort)
        print("")


main()
