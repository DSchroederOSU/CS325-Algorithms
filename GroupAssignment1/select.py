#!/usr/bin/python
""" merge and sort algs take from
https://gist.github.com/anirudhjayaraman/975675ce65f65b73606c#file-mergesort-py
"""
import struct
import sys
sys.setrecursionlimit(1000000)

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """

    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x)/2)
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)

def read_file(file_number, index):
    filename = ''.join([str(file_number+1), ".dat"])
    with open(filename, mode='rb') as file:  # b is important -> binary
        v = index
        size_ = 4
        while True:
            file.seek(v * size_)

            try:
                return struct.unpack('>I', file.read(size_))[0]

            except:
                return -1


#  code for merge
def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


#  this binsearch seems to be working correctly,
def binSearch(filenumber, elem, start, end):
    if start > end:
        return end
    mid = int((start + end) / 2)
    if read_file(filenumber, mid) < elem:
        return binSearch(filenumber, elem, mid + 1, end)
    elif read_file(filenumber, mid) > elem:
        return binSearch(filenumber, elem, start, mid - 1)
    else:
        return mid


def getMid(indexes):
    max = getLength(indexes[0])
    id = 0
    for i in range(1, len(indexes)):  # O(m)
        if getLength(indexes[i]) > 1:
            length = getLength(indexes[i])
            if length > max:
                max = length
                id = i
    return read_file(id, int((indexes[id][0] + indexes[id][1]) / 2))


def getLength(range):

    return (range[1] - range[0]) + 1


def split(indexes, m, mid, less, greater, k):
    for i in range(0, m):
        if getLength(indexes[i]) > 1:  # size > 1
            break
        elif i == m-1 and getLength(indexes[i]) <= 1:  # all arrays are size 1
            # merge all arrays and find kth elements
            merged = []
            for i in range(0, m):
                merged.append(read_file(i, indexes[i][0]))

            f = open("output.txt", "w+")
            f.write(str(mergesort(merged)[k-1]))
            exit(0)

    lower_indeces = []

    for i in range(0, m):
        index = binSearch(i, mid, indexes[i][0], indexes[i][1]) + 1  # index is zero but value should be 1 ( 1 elem )
        lower_indeces.append(index - 1)
        less += index - indexes[i][0]
        greater += (indexes[i][1] - index) + 1

    if k <= less:  # chop off upper half of array
        for i in range(0, m):
            if getLength(indexes[i]) >= 1:
                indexes[i][1] = lower_indeces[i]
            elif getLength(indexes[i]) == 1:
                if read_file(i, indexes[i][0]) <= mid:
                    k += 1
        split(indexes, m, getMid(indexes), 0, 0, k)

    if k > less:  # now k > L so chop lower half of array and reduce k
        k -= less
        for i in range(0, m):
            if getLength(indexes[i]) >= 1:
                indexes[i][0] = lower_indeces[i] + 1
            elif getLength(indexes[i]) == 1:
                if read_file(i, indexes[i][0]) <= mid:
                    k += 0

        split(indexes, m, getMid(indexes), 0, 0, k)


def newSelect():
    input_file = open("input.txt", "r")
    input_args = input_file.read().split(',')

    """ 0 = m, 1 = n, 2 = k"""
    num_files = int(input_args[0])
    arr_length = int(input_args[1])
    kth_smallest = int(input_args[2])

    indexes = []
    for i in range(0, num_files):
        indexes.append([0, arr_length-1])

    mid_value = read_file(0, int((arr_length)/2))
    split(indexes, num_files, mid_value, 0, 0, kth_smallest)


#  main()

newSelect()