from collections import deque
    
def reverse_numbers(i, j, numbers):
    numbers_f = []
    numbers_b = []
    numbers_m = []
    flag = False
    for index in range(len(numbers)):
        if index < i:
            numbers_f.append(numbers[index])
        if index > j:
            numbers_b.append(numbers[index])
        if (i <= index <= j) and (flag == False):
            flag = True
            for k in range(i, j + 1):
                numbers_m.append(numbers[k])
            numbers_m.reverse()
    return numbers_f + numbers_m + numbers_b
        
        
N, M = map(int, input().split())
numbers = [i for i in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    numbers = reverse_numbers(i, j, numbers)

for index in range(1, len(numbers)):
    print(numbers[index], end=" ")