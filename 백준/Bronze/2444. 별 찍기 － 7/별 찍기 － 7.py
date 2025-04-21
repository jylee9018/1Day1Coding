N = int(input())

numbers_f = []
numbers_b = []
for i in range(1, N + 1):
    numbers_f.append(2 * i - 1)
for i in range(N - 1, 0, -1):
    numbers_b.append(2 * i - 1)

space = N - 1
for number in numbers_f:
    print(" " * (space) + "*" * number)
    space = space - 1

space = 1
for number in numbers_b:
    print(" " * (space) + "*" * number)
    space = space + 1