import numpy as np

H, W, X, Y = map(int, input().split())
A = np.array([np.array(list(input())) for _ in range(H)])
#A = [list(input()) for _ in range(H)]

#print(A)

#print(A[X-1][Y-1])

count = 1

VP = A[0:X-1, Y-1]
VM = A[X:, Y-1]
SP = A[X-1, 0:Y-1]
SM = A[X-1, Y:]

#print(VP)
#print(VM)
#print(SP)
#print(SM)

for i in reversed(range(len(VP))):
  if VP[i] == '#':
    break
  count += 1

for i in range(len(VM)):
  if VM[i] == '#':
    break
  count += 1

for i in reversed(range(len(SP))):
  if SP[i] == '#':
    break
  count += 1

for i in range(len(SM)):
  if SM[i] == '#':
    break
  count += 1

print(count)
