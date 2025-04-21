# def reverse_numbers(i, j, numbers):
#     numbers_f = []
#     numbers_b = []
#     numbers_m = []
#     flag = False
#     for index in range(len(numbers)):
#         if index < i:
#             numbers_f.append(numbers[index])
#         if index > j:
#             numbers_b.append(numbers[index])
#         if (i <= index <= j) and (flag == False):
#             flag = True
#             for k in range(i, j + 1):
#                 numbers_m.append(numbers[k])
#             numbers_m.reverse()
#     return numbers_f + numbers_m + numbers_b
        
        
# N, M = map(int, input().split())
# numbers = [i for i in range(N + 1)]

# for _ in range(M):
#     i, j = map(int, input().split())
#     numbers = reverse_numbers(i, j, numbers)

# for index in range(1, len(numbers)):
#     print(numbers[index], end=" ")

# 위의 풀이는 비효율적이다.
# 1. 불필요한 리스트 생성
#   - numbers_f, numbers_m, numbers_b 등 총 세 개의 리스트를 만들어서 이어붙이는 방식은 
#     메모리 사용도 늘어나고, 처리 속도도 느려질 수 있다.
# 2. 불필요한 반복문과 조건문
#   - for 루프 안에서 flag를 써서 복잡하게 조건을 확인하고 있는데, 
#     Python의 슬라이싱을 활용하면 훨씬 간단하게 구현 가능.

# 슬라이싱을 이용!
# 슬라이싱(Slicing) 은 문자열(String), 리스트(List), 튜플(Tuple) 등 시퀀스(Sequence) 자료형에서 모두 사용할 수 있다.

N, M = map(int, input().split())
numbers = [i for i in range(N + 1)]  # 0번 인덱스는 사용하지 않음

for _ in range(M):
    i, j = map(int, input().split())
    numbers[i:j+1] = reversed(numbers[i:j+1])  # 슬라이싱과 reversed 사용

print(*numbers[1:])  # 1번부터 출력