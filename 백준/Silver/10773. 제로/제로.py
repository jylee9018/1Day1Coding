K = int(input())

numbers = []
for i in range(K):
    number = int(input())
    if number == 0:
        numbers.pop()
    else:
        numbers.append(number)

answer = sum(numbers)
print(answer)