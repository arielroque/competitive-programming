
numbers = []
primes = [1,3,5,7]

def get_unique_number(n):
    
    if(n in primes):
        print (n)
        return
   
    result = ""

    for i in range(9,0,-1):
        if (n >= i):
            n-=i
            result+=str(i)
           
    if(n != 0):
        print (-1)
        return
    
    print(result[::-1])


n = int(input())

for i in range(n):
    numbers.append(int(input()))

for i in numbers:
    get_unique_number(i)

