X = int(input())

i = 0
while X - i*100 < 0:
    i += 1

print(i*100-X)