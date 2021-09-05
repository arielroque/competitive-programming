
s=""
for _ in " "*int(raw_input()):
  n,r=map(int,raw_input().split())
  a=sorted(set(map(int,raw_input().split())))[::-1]
  cnt=0
  for i in a:
    if i<=cnt*r:
      break
    cnt+=1
  s+=str(cnt)+'\n'
print s