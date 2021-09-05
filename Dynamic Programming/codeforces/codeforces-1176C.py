def minimum(n, l):
    nums = [4, 8, 15, 16, 23, 42]
    aux = [0,0,0,0,0,0]
 
    for e in l:
        i = nums.index(e)
        if (i == 0):
            aux[i] += 1

        elif (aux[i-1] > 0):
            aux[i-1] -= 1
            aux[i] += 1
 
    res = n - aux[5] * 6
    return res
 
 
n = int(input())
l = list(map(int, input().split()))

print(minimum(n, l))