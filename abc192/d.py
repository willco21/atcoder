def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out
 
 
XM = [int(input()) for _ in range(2)]

X = XM[0]
M = XM[1]
xl =  [int(x) for x in list(str(X).zfill(len(str(X))))]
#print(xl)
xl.sort(reverse=True)
d = xl[0]
#print(d)

d += 1

Xn = int(str(X), d)
#print(Xn)
i = 0

while Xn <= M:
    d += 1
    i += 1
    Xn = int(str(X), d)

print(i)
