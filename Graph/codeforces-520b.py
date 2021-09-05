n, m = map(int, input().split())

result = 0

if(n > m):
    print(n-m)
else:
    while(m-n):

        if(m % 2 == 0 and m > n):
            m = m/2
            result+=1
        else:
            if(n >= m):
                result += (n-m)
                break
            m = (m+1)//2
            result += 2
    print(int(result))
