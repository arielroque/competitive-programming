found = False
values = []

def search(n, y, values):
    global found

    if(found):
        return

    if(n == y):
        found = True
        print("YES")
        print(len(values))
        print(*values)

    if(n > y):
        return

    values.append(2 * n)
    search(2 * n, y, values)
    values.pop()

    values.append(10 * n + 1)
    search(10 * n + 1, y, values)
    values.pop()


x, y = map(int, input().split())

values.append(x)

search(x, y, values)

if(not found):
    print("NO")
