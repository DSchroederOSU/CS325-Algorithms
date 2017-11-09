#!/usr/bin/python3




def knapsack(n, weight, w, v):
    if n == -1:
        return 0
    if weight <= 0:
        return 0

    #  need to check that we can take the nth item and not be past weight
    if weight - w[n] >= 0:
        retVal = max(knapsack(n-1, weight, w, v), knapsack(n-1, weight - w[n], w, v) + v[n])
    else:
        retVal = knapsack(n-1, weight, w, v)
    return retVal



w = [10, 20, 30]
v = [60, 100, 120]
b = 40


a = []
for i in range(0, len(v)):

    a.append(v[i]/w[i])

print(len(a)-1)
print(knapsack(len(a)-1, b, w, v))