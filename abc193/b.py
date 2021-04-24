N = int(input())
APX_list = [list(map(int, input().split())) for _ in range(N)]

#print(APX_list)

newAPX = [[a[0] * 2, a[1], a[2]] for a in APX_list]

result = []

for apx in newAPX:
    buy = apx[0] // 2
    #print(buy)
    #print(apx[2])
    if apx[2] - buy > 0:
        result.append(apx[1])
    else:
        continue
        #result.append(False)

if result:
    print(min(result))
else:
    print(-1)

１台減る
0.5 / 1,5 / 2.5
10倍-> 5 / 15 / 25
2倍 -> 1 / 3 / 5
4倍 -> 2 / 6 / 10

小数点計算はやめたい

3
3 9 5
4 8 5
5 7 5


