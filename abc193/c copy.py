N = int(input())

result_base = [*range(4, N+1)]
print(result_base)

K = [[a**b for b in range(2, N+1)] for a in range(2, N+1)]

print(K)

OK = 0

i = 1

for k in K:
    print(k[-i])
    print(k.index(k[-i]))
    if k[-i] <= N:
        print(k.index(k[-i]))
        OK += k.index(k[-i]) + 1
        i = 1
    else:
        i += 1
        continue

NG = N - OK
print(NG)
