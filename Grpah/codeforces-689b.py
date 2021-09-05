n = int(input())
a = list(map(int,input().split()))
energy = [-1] * n
energy[0] = 0
pos = [0]
 
for i in pos:
    for v in [i - 1, i + 1, a[i] - 1]:
        if v >= 0 and v < n and energy[v] == -1:
            energy[v] = energy[i] + 1
            pos.append(v)
 
print(*energy)
