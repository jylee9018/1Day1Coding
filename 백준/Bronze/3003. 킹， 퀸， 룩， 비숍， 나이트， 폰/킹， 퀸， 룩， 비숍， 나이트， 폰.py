# 1 1 2 2 2 8

a = list(map(int, input().split()))
b = [1, 1, 2, 2, 2, 8]

for i in range(len(b)):
    print(b[i] - a[i], end=" ")