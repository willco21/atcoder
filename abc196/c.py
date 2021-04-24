import itertools
from itertools import product

N = int(input())
#f = ["11", "22", "33", "44", "55", "66", "77","88", "99"]

#base_count = 

result = [[]]

for n in range(0, len(N)//2):
  if n == 0:
    part = [''.join(p) for p in product(range(1,10), list("123456789"))]
  else:
    part = [''.join(p) for p in product(result[n], list("1234567890"))]
  for p in part:
    if (int(p+p) > N):
      break
    else:
      result[n].extend(p+p)

print(len(result))

----

N = int(input())
#f = ["11", "22", "33", "44", "55", "66", "77","88", "99"]

#base_count =

result = [[]]
#result[0].extend(list("123456789"))

print(len(str(N)))

for n in range(0, len(str(N))//2):
  if n == 0:
    part = list("123456789")
  else:
    for p in product(result[n-1], list("1234567890")):
      for s in p[0]
list(str(s))
#part = [''.join(p) for p in product(result[n-1], list("1234567890"))]
print(part)
for p in part:
    if (int(p) > N):
      break
    else:
      result[n].append(p+p)

print(result)

print(len(list(itertools.chain.from_iterable(result))))


----
1 <= x <= N
偶数桁
-> 必ず分けられる

分けたうちの前半の数字がx

これを見たす「xの個数」を答えろ


33
11 / 22 / 33


1333

11 22 33  44 55 66 77 88 99 
1010 1111 1212 1313

10000

1010 1111 1212 1313 1414 1515 1616 1717 1818 1919
2020 2121 2222 2323 2424 2525 ...
3030 
9090 9191 9292 9393 9494 9595 9595 9797 9898 9999

100000

100100 101101 102102 103103
110110 111111 112112

↓ 
1つ前の桁の数に対して操作すれば次の数がでる
-> 間に同じ数字をはさむ
11 -> 0はさむ -> 1010
→11からはさむことで生まれる数は10 個
1212 -> 3はさむ -> 123123
→1212からはさむことで生まれる数は10 個

↓
4桁以降は〇桁の数字一覧*10個存在

よって
2桁-> 9個

4桁→9*10 = 90

6桁-> 90 * 10 = 900

あとはNの桁数の数字をどう出すか

Nが何桁かをだす
2 4 6 8 10 12桁のうちN桁以下のものを対象

Nが上記桁数の場合、順番に計算

