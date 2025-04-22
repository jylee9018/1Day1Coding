word = input()

idx, cnt = 0, 0
while idx < len(word):
    # 문자열 슬라이싱 이용
    if word[idx:(idx+1)+1] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
        idx_step = 2
        cnt += 1
    elif word[idx:(idx+2)+1] in ["dz="]:
        idx_step = 3
        cnt += 1
    else:
        idx_step = 1
        cnt += 1
    idx += idx_step

print(cnt)