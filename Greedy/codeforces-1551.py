import math

def get_coins(x):

    x1 = None
    x2 = None

    if(x%3 == 1):
        x2 = x/3
        x1 = x2+1
    
    elif (x%3 == 2):
        x2 = (x/3)+1
        x1 = x2-1
    
    else:
         x1=x2=x/3
  
    x1 = math.floor(x1)
    x2 = math.floor(x2)

    return x1, x2


n = int(input())

for i in range(n):
    x = int(input())
    v1, v2 = get_coins(x)
    print(v1, v2)
