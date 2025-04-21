array = list(map(int, input().split()))
# array = [6, 2, 5]
a = array[0]
b = array[1]
c = array[2]

if a == b == c:
    answer = 10000 + a * 1000
elif (a == b) or (a == c):
    answer = 1000 + a * 100
elif (b == c):
    answer = 1000 + b * 100
else:
    answer = max(array) * 100
    
print(answer)