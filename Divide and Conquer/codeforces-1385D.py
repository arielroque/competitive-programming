def solution(inp, current_char='a'):
    length = len(inp)

    if (length == 1):
        return 0 if inp == current_char else 1

    next_char = chr(ord(current_char)+1)

    return min(solution(inp[length//2:], next_char) + sum(map(lambda x: 0 if x == current_char else 1, inp[:length//2])),
    solution(inp[:length//2], next_char) +
             sum(map(lambda x: 0 if x == current_char else 1, inp[length//2:])))

t = int(input())

for i in range(0,t):
    n = int(input())
    value = input()
    print(solution(value))
