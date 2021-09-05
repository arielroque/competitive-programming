x = 1000 * [0]
y = 1000 * [0]
v = 100 * [False]


def search(j):
    v[j] = True
    for i in range(n):
        if (not v[i] and (x[i] == x[j] or y[i] == y[j])):
            search(i)

n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    x[i] = a
    y[i] = b

result = 0

for i in range(n):
    if (not v[i]):
        result+=1
        search(i)

print(result -1)


