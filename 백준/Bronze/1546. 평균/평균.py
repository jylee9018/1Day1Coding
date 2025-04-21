N = int(input())
numbers = list(map(int, input().split()))
    
M = max(numbers)

numbers_manuplated = []
for i in range(len(numbers)):
    numbers_manuplated.append(numbers[i] / M * 100)

answer = sum(numbers_manuplated) / len(numbers)
print(answer)