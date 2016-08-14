# -*-  coding: utf-8 -*-
"""
A non-empty zero-indexed array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)
that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.


A = [2, 3, 1, 5]
A2 = [2, 3, 1, 4]
A3 = [2, 3, 5, 4]
A4 = [2,3]
A4 = [2,2,2,2,2,2,2]
A5 = [1, 2, 3, 5, 4]



def solution(A):
    # this was 80%
    # https://codility.com/demo/results/trainingCE7BF8-XZC/
    # return 1 if len(A) == sorted(A)[-1] else 0
    ln = len(A)
    if ln == sorted(A)[-1]:
        if ln == len(set(A)):
            return 1
    return 0

print(solution(A))
print(solution(A2))
print(solution(A3))
print(solution(A4))
print(solution(A5))
