# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

number1 = input()
number2 = input()

print(int(number1) * int(number2[-1]))
print(int(number1) * int(number2[-2]))
print(int(number1) * int(number2[-3]))
print((int(number1) * int(number2[-1])) + (int(number1) * int(number2[-2]) * 10) + (int(number1) * int(number2[-3]) * 100))
