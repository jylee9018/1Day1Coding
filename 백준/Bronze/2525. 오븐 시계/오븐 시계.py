H, M = map(int, input().split())
C = int(input())

def MtoH(m):
    tH = str(m // 60)
    tM = str(m % 60)
    return tH, tM

tH, tM = MtoH(C)

dH = H + int(tH)
dM = M + int(tM)

if dM > 59:
    dM = dM - 60
    dH = dH + 1

if dH > 23:
    dH = dH % 24

print(dH, dM)