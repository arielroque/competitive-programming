 v = 0
 par = []

def init(siz):
     v = siz 
     par.clear()

     for i in range(v):
         par.append(-1)

     return

def root(x):
    if (par[x] < 0):
        return x 
    
    r = root(par[x])
    par[x] = r

    return r

def size(x):
    return -par[root(x)]

def same(x,y):
    return root(x) == root(y)

def unite(x,y):
    rx = root(x)
    ry = root(y)

    if(rx == ry):
        return False
    
    if (par[rx] > par[ry]):
        rx ^= ry
        ry ^= rx
        rx ^= ry
    
    par[rx] += par[ry]
    par[ry] = rx

    return True

n,m = map(int,input().split())

s = [list(input()) for _ in range(n)]

result = "No"

init(n*m)

for i in range(n):
    for j in range(m):
        if(i <n -1):
            if(s[i][j] == s[i+1][j]):
                if not unite(i*m+j,(i+1)*m + j):
                    result = "Yes"

        if (j < m -1):
            if (s[i][j] == s[i][j+1]):
                if not unite(i*m+j,i*m+j+1):
                    result = "Yes"

print(result)

