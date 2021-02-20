S = input()

m = list(S)

i = 1

while m < len(m):
    if i % 2 == 0:
        if not m.islower():
            print("No")
            exit()
            break
    else:
        if not m.isupper():
            print("No")
            exit()
            break

print("Yes")

