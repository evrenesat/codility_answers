# -*-  coding: utf-8 -*-
"""
A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)
that, given a zero-indexed array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Assume that:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

A = [2, 3, 1, 5]
A2 = [2, 3, 1, 4]
A3 = [2, 3, 5, 4]
A4 = [2]
A5 = []


def solution(A):
    for i, v in enumerate(sorted(A), 1):
        if i != v:
            return i
    ln_p_1 = len(A) + 1
    if ln_p_1 not in A:
        return ln_p_1


print(solution(A))
print(solution(A2))
print(solution(A3))
print(solution(A4))
print(solution(A5))
