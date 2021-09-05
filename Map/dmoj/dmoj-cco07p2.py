def is_identical_right(snow1, snow2, start):

    for i in range(len(snow1)):
        if(snow1[i] != snow2[(start + i) % 6]):
            return False
    return True


def is_identical_left(snow1, snow2, start):

    for i in range(6):

        snow2_index = start - i

        if(snow2_index < 0):
            snow2_index = snow2_index + 6

        if(snow1[i] != snow2[snow2_index]):
            return False
    return True


def is_identical(snow1, snow2):
    for i in range(6):
        if(is_identical_right(snow1, snow2, i)):
            return True

        if(is_identical_left(snow1, snow2, i)):
            return True

    return False


def check_snowflakes(data):
    for i in data:
        similars = data[i]
        for j in range(len(similars)):
            for k in range(j+1,len(similars)):
                if(is_identical(similars[j], similars[k])):
                    print("Twin snowflakes found.")
                    return



    print("No two snowflakes are alike.")

def check_snowflakes1(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if(is_identical(data[i], data[j])):
                print("Twin snowflakes found.")
                return

    print("No two snowflakes are alike.")


n = int(input())
data = {}


for i in range(n):
    snow = list(map(int, input().split()))
    sum_snow = sum(snow)

    if(sum_snow not in data):
        data[sum_snow] = []

    data[sum_snow].append(snow)

check_snowflakes(data)
