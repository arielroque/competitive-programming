from collections import deque

def solve(n, arr):
    l, r, depth = 0, n, 0
    queue = deque()
    ans = [-1 for i in range(n)]
    queue.append((l, r, depth))

    while len(queue) > 0:
        l, r, depth = queue.popleft()

        if (l == r):
            continue

        max_elem = -1
        max_pos = -1

        for i in range(l, r):
            if (arr[i] > max_elem):
                max_elem = arr[i]
                max_pos = i

        ans[max_pos] = depth
        queue.append((1, max_pos, depth+1))
        queue.append((max_pos+1, r, depth+1))

        return ans


j = int(input())

for i in range(j):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = solve(n, arr)
    print(' '.join(list(map(str, ans))))
