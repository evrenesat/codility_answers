# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
import random

A = []
for i in range(999999):
    A.append(
        random.randint(-2147483648, 2147483647))
A.append(22)
A.extend(A[:-1])
# A = [-1, 3, -4, 5, 1, -6, 2, 1]

def solution(A):
    ln = len(A)
    x, y, t = 0, 0, sum(A)
    for i in xrange(ln):
        if i == ln:
            break
        if i > 0:
            x += A[i - 1]
        y = t - (x + A[i])
        if y == x:
            return i
    return -1


print("starting")
print(solution(A))
print(solution([]))
