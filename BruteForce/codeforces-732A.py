price, r = map(int, input().split())

cont = 1

while(True):

    p = price * cont

    if(str(p)[-1] == str(r)):
        break

    if(p % 10 == 0):
        break

    cont = cont + 1

print(cont)
