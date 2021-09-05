def par(p):
    if p != root[p]:
            root[p] = par(root[p])
    return root[p]
 
 
n, m, k = map(int, input().split())
special = map(int, input().split())
 
root = [p for p in range(n+1)]
 
for i in range(m):
	u,v = map(par, map(int, input().split()))
	root[v] = u
 
sz = [0 for i in range(n+1)]
 
for i in range(n+1):
	sz[par(i)] += 1
 
leftover = n
result = 0
largest = 0
 
for x in special:
	d = par(x)
	largest = max(largest, sz[d])
	result += sz[d] * (sz[d] - 1) // 2
	leftover -= sz[d]
 
result -= largest * (largest - 1) // 2
result += (largest+leftover) * ((largest+leftover) - 1) // 2
result -= m
 
print(result)