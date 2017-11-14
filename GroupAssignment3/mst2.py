#!/usr/bin/python

# importing "heapq" to implement heap queue
import heapq

global myedges

# READ input.txt
# 1st line 0 < n < 30
# rest lines n lines of n values delim ',' 0 < n < 30
with open('input.txt', 'r') as f:
    n = int(f.readline())
    f.close()


def heapInsert(v, arr, heap):
    for i in range(0, len(arr)):
        if i != v:
            heapq.heappush(heap, (arr[i], (v, i)))


def readRow(row):
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        return [int(x) for x in lines[row].strip('\n').split(',')]



def primMST(heap, e):
    (w, (v1, v2)) = e
    MSTtotal = 0
    # while heap is not empty

    while len(heap) > 0:
        (weight, (v, u)) = heapq.heappop(heap)  # pop the minimum weight edge (root) from heap

        if v1 != v or v2 != u:
            #  look at both vertices of the edge we just pulled from the heap
            if label[u] != label[v] and label[v] == 1:  # if the vertex 'v' is already in MST
                label[u] = 1  # add 'u' to the MST
                heapInsert(u, readRow(u+1), myHeap)  # add all the edges of the vertex we added into heap
                MSTtotal += weight  # add the weight to MST total weight
            elif label[u] != label[v] and label[u] == 1:  # if the vertex 'u' is already in MST
                label[v] = 1  # add 'v' to the MST
                heapInsert(v, readRow(v+1), myHeap)  # add all the edges of the vertex we added into heap
                MSTtotal += weight  # add the weight to MST total weight
    return MSTtotal


with open('input.txt', 'r') as f:
    n = int(f.readline())
    adjMatrix = [line.strip('\n').split(',') for line in f]
    adjMatrix = [[int(y) for y in x] for x in adjMatrix]
    f.close()

allEdges = []
heapq.heapify(allEdges)
for x in range(0, n):
    heapInsert(x, readRow(x + 1), allEdges)

print(allEdges)

totals = []
heapq.heapify(totals)




for edge in allEdges:
    myHeap = []

    # using heapify to convert list into heap
    heapq.heapify(myHeap)

    # insert the first vertex into the heap with all of its its edges
    # i.e. the first row if the adjacency matrix
    heapInsert(0, readRow(1), myHeap)
    label = [0 for x in range(n)]

    label[0] = 1

    total = primMST(myHeap, edge)

    heapq.heappush(totals, total)

one = heapq.heappop(totals)
two = -1
three = -1
while len(totals) != 0:
    test = heapq.heappop(totals)
    if test != one:
        two = test
        break

while len(totals) != 0:
    test = heapq.heappop(totals)
    if test != two:
        three = test
        break

print(one)
print(two)
print(three)