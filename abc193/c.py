N = int(input())
OK = []

a = 2
b = 2

while a**2 <= N:
    if a**b <= N:
        print(a**b)
        OK.append(a**b)
        b += 1
    else:
        print(a**b)
        a += 1
        b = 2

NG = N - len(list(set(OK)))
print(NG)
    
----


for a in range(2, N+1):


#print(K)

OK = 0

i = 1

for k in K:
    if k[0] > N:
        continue
    if k[-1] <= N:
        OK += k.index(k[-1]) + 1
    for n in reversed(k):
        if n <= N:
            #print(k.index(n))
            OK += k.index(n) + 1
            break

NG = N - OK
print(NG)



#for n in range(4, N+1):
    




----

2 <= a, b <= N
a**b > N

a**b が整数になる

1,2,3は絶対に表せない

全探索してもいいけど、なんかルールない？


2**2 = 4
2**3 = 8
2**4 = 16

3**2 = 9
3**3 = 27
3**4 = 81

ある数がOKのとき、それをaでかけた奴がOKかどうか

でかい数字を出せば、それをaで割った数が

