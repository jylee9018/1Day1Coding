# 앞에서부터 문자를 하나씩 확인하면서,
# 1) 이전 문자와 다르면
# 2) 그 문자가 이미 나왔던 문자라면
# 그룹 단어가 아니다.

def check_groupword(word):
    seen = set()
    prev = ''
    for char in word:
        if char != prev:
            if char in seen:
                return False
            seen.add(char)
        prev = char
    return True

N = int(input())

count = 0
for _ in range(N):
    word = input()
    if check_groupword(word):
        count += 1

print(count)
