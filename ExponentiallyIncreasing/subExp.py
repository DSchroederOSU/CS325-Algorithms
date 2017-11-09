#!/usr/bin/python3



def subExp(n, arr):
    print(n)
    if n == 0:
        retVal = 0

    elif arr[n-1]*2 < arr[n]:
        retVal = max(1, subExp(n-1, arr) + 1)

    else:
        retVal  = subExp(n-1, arr)

    return retVal


A = [1, 3, 5, 11, 7, 25, 53]

print(subExp(6, A))
