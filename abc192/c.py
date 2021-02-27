def kaprekar_function(n, digits, is_reverse):
    l =  [int(x) for x in list(str(n).zfill(digits))]
    l.sort(reverse=is_reverse)
    return l
    
def kaprekar_routine(n, is_reverse):
    pre = n
    digits = len(str(n))
    suc = kaprekar_function(n, digits=digits, is_reverse=is_reverse)
    print(suc)
    return suc

N, K = map(int, input().split())

a = [N]

for i in range(K):
    a.append(kaprekar_routine(a[i],True) - kaprekar_routine(a[i],False))


print(a[K])


