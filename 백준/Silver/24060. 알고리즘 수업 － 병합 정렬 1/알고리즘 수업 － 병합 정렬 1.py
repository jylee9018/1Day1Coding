# 배열을 반씩 나누는 재귀 함수
def merge_sort(array, p, r):
    # 종료 조건: 1개짜리 배열이 되었을 때
    if p == r:
        return
    
    q = (p + r) // 2
    
    merge_sort(array, p, q)
    merge_sort(array, q + 1, r)
    merge(array, p, q, r)


def merge(array, p, q, r):
    i = p       # 좌 리스트 시작 인덱스  
    j = q + 1   # 우 리스트 시작 인덱스
    
    tmp = []
    global K
    global count
    while (i <= q) and (j <= r):
        # 오름차순 정렬
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1

    while i <= q:
        tmp.append(array[i])
        i += 1
    
    while j <= r:
        tmp.append(array[j])
        j += 1
    
    for i in range(len(tmp)):
        array[p + i] = tmp[i]
        # print(array)
        
        count += 1
        if count == K:
            print(array[p + i])
            break


N, K = map(int, input().split())
A = list(map(int, input().split()))
# # 입력 예시
# N, K = 5, 7
# A = [4, 5, 1, 3, 2]

count = 0
merge_sort(A, 0, len(A) - 1)

# 저장 횟수가 K보다 작으면 -1 출력
if count < K:
    print(-1)