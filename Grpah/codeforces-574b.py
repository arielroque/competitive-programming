import math 

n,m = map(int,input().split())

network=[[]for _ in range(n)]
sums = [0]*n

vis = [False]*n
result = math.inf

for _ in range(m):
    a,b = map(int,input().split())
    network[a-1].append(b-1)
    network[b-1].append(a-1)
    sums[a-1]+=1
    sums[b-1]+=1

for i in range(n):
    vis[i] = True
    for neighbor1 in network[i]:
        if not vis[neighbor1]:
            for neighbor2 in network[neighbor1]:
                if (neighbor2 != i and i in network[neighbor2]):
                    if (result > sums[i] + sums[neighbor1] + sums[neighbor2]):
                        result= sums[i]+sums[neighbor1]+ sums[neighbor2]
                        pass
                        break
if(result < math.inf):
    print(result-6)
else:
    print(-1)
                

