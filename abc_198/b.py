#!/usr/bin/python3
from itertools import groupby


N = input()
L = [int(n) for n in list(N)]

#print(L)

if L[0] != L[-1] and L[-1] != 0:
    print("No")
    exit(0)

#print(len(L))

if L[-1] == 0:
  gr = groupby(L)
  out = [len(list(group)) for i, group in gr]
  del L[-(out[-1]):]

#print(L)

for l in range(len(L)//2):
  if L[l] != L[-(l+1)]:
    print("No")
    exit(0)

print("Yes")




#---
#0個以上の 0 をつけることで、回文にすることはできますか？
#
#* n[0] == n[-1]
#* n[-1] == 0
#
#あとはあるかずAに対して
#n[A] == n[-(A+1)]
#が成り立つことを確認
#

#forは前半のみにする %2
#8桁 -> 0~3
#9桁　-> 0~3
#
#後ろに0が続く場合はイケる
#
#
#1233456700000000
#
