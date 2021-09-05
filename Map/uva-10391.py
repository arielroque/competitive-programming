import sys

lista = set()
dic = {}
response = []

while True:

    entrada = sys.stdin.readline().strip()

    if(not entrada):
        break

    lista.add(entrada)


for w in lista:
    for i in range(1, len(w) + 1):
        if(w[:i] in lista and w[i:] in lista):
            response.append(w)
            break

for i in sorted(response):
    print(i)
