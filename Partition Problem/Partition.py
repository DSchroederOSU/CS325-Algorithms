#!/usr/bin/python3

def subSumDP(arr):
    n = len(arr)
    sum = 0
    for i in range(0, n):
        sum += arr[i]

    sum = int(sum/2)
    mem = []

    for i in range(0, sum+1):
        if i == 0:
            mem.append([True])
        else:
            mem.append([False])
        for j in range(1, n + 1):
            if i == 0:
                mem[i].append(True)
            else:
                mem[i].append(False)

    for i in range(1, sum+1):
        for j in range(1, n + 1):
            mem[i][j] = mem[i][j-1]
            if i >= arr[j-1]:
                mem[i][j] = mem[i][j] or mem[i - arr[j-1]][j-1]

    # for i in range(0, sum+1):
        # print(mem[i])
    return mem[sum][n]


def isSubsetSum(arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    if arr[n - 1] > sum:
        return isSubsetSum(arr, n - 1, sum)

    return isSubsetSum(arr, n - 1, sum) or isSubsetSum(arr, n - 1, sum - arr[n - 1])




arr = [3, 1, 1, 2, 2, 1]
sum = 10
n = len(arr)


print(isSubsetSum(arr, n, sum/2))