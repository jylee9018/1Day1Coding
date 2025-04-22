def recursion(s, l, r):
    global count
    count += 1
    
    # → 왼쪽 인덱스(l)가 오른쪽 인덱스(r)에 도달하거나 지나쳤다는 것
    # → 모든 문자가 서로 같았다는 뜻이므로 팰린드롬이다!
    if l >= r:    
        return 1  # 팰린드롬임
    elif s[l] != s[r]:
        return 0  # 서로 다른 문자 → 팰린드롬 아님
    else:
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


T = int(input())
for _ in range(T):
    s = input()
    count = 0
    print(isPalindrome(s), count)