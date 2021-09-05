n = int(input())
m = 99999
ans = 0

for i in range(n):
    a,p = [int(x) for x in input().split()]
    m = min(m,p)
    ans += (a*m)

print(ans)