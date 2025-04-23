N = input()

numbers = []
for c in N:
    numbers.append(int(c))

numbers.sort(reverse=True)

for n in numbers:
    print(n, end="")