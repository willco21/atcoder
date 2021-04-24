#!/usr/bin/python3

import collections

N = int(input())
A = list(map(int, input().split()))

L1 = A[0::2]
L2 = A[1::2]

L1c = collections.Counter(L1)
L2c = collections.Counter(L2)

print(L1c)
print(L2c)

L1_most = L1c.most_common()
L2_most = L2c.most_common()

print(L1_most[0][1])
print(L2_most[0][1])

if (len(set(A)) == 1):
  print(len(L1))
elif(L1_most[0][0] != L2_most[0][0]):
  print(len(L1)-L1_most[0][1] + len(L2)-L2_most[0][1])
else:
  count_L1firstL2 = len(L1)-L1_most[0][1] + len(L2)-L2_most[1][1]
  count_L1secondL2 = len(L1)-L1_most[1][1] + len(L2)-L2_most[0][1]
  print(min(count_L1firstL2, count_L1secondL2))
