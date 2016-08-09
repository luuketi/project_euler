# Project Euler
# Problem 117 - 35%

numbers = [1,2,3,4]

combinations = {}

def comb(sum_total):
    z = 0
    for i in numbers:
        if i < sum_total:
            if (i, sum_total) not in combinations:
                combinations[(i, sum_total)] = comb(sum_total-i)
            z += combinations[(i, sum_total)]
        elif i == sum_total:
            z += 1
    return z

print comb(5)
print comb(50)
