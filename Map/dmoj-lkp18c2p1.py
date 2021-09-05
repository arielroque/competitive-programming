n, m = [int(x) for x in input().split()]
lines = [int(x) for x in input().split()]

output = ""
lines.sort()

for i in range(m):
    small_number = min(lines)
    index = lines.index(small_number)
    output+=f"{lines[index]}\n"
    lines[index]+=1
    
print(output[:-1])

