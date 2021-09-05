ex, ey = map(int, input().split())

c = [0] * (ex + 1)

for l in range(ex + 1):
    c[l] = [1] * (ex + 1)

for i in range(ey):
    a, b = map(int, input().split())
    c[a][b] = c[b][a] = 2


x, v, i = 3 - c[1][ex], [0] * (ex + 1), 1
d = [ex + 1] * (ex + 1)
time =  d[1] = 0
 
while i != ex:

    v[i] = 1

    for j in range(1, ex + 1):
        if v[j] == 0 and c[i][j] == x and d[j] > d[i] + 1:
            d[j] = d[i] + 1

    m = ex + 1

    for j in range(1, ex + 1):
        if v[j] == 0 and d[j] < m:
            m = d[j]
            i = j

    if m == ex + 1:
        time = -1
        break

    elif i == ex:
        time = d[ex]
        break
 
print(time)