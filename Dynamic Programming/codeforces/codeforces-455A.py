
n = input()
l = list(map(int, input().split()))
 

max_value = max(l) + 1
memorization = [0] * max_value
 
for i in l:
    memorization[i] += i
 
for i in range(2, max_value):
    memorization[i] = max(memorization[i-1], memorization[i] + (memorization[i-2]))
 

print (memorization[-1])