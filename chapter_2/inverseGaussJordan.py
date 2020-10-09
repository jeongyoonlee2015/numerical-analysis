#from 코딩도장

n = int(input("행렬의 크기를 입력하세요:"))
row = []
col = []
for x in range(n):
    for y in range(n):
        row.append(float(input("{}행{}열 원소를 입력하세요".format(x + 1, y + 1))))
    col.append(row)
    row = []
for x in range(n):
    print(col[x])
inv = []
for x in range(n):
    for y in range(n):
        row.append(0)
    inv.append(row)
    row = []
for x in range(n):
    inv[x][x] = 1
print(inv)

aug = []
for x in range(n):
    aug.append(row)
for x in range(n):
    aug[x] = col[x] + inv[x]
print(aug)

k = 1
a = []
b = []

k = 1
for t in range(n-1):
    while aug[t][t] == 0 and k != n:
        a = aug[t]
        b = aug[k]
        aug[t] = b
        aug[k] = a
        k += 1
    k = t + 2
    if aug[t][t] == 0:
        print("역행렬이 존재하지 않습니다.")
    else:
        for x in range(t + 1,n):
            c = (aug[x][t]/aug[t][t])
            for y in range(0, 2 * n):
                aug[x][y] -= c * aug[t][y]

for x in range(n):
    if aug[x][x] == 0:
        print("역행렬이 존재하지 않습니다.")
        break
for x in range(n):
    print(aug[x])

for t in range(1, n):
    for x in range(0, t):
        c = (aug[x][t]/aug[t][t])
        for y in range(0, 2 * n):
            aug[x][y] -= c * aug[t][y]
for x in range(n):
    print(aug[x])

for x in range(n):
    c = aug[x][x]
    for y in range(2 * n):
        aug[x][y] /= c
for x in range(n):
    print(aug[x][n: 2 * n])