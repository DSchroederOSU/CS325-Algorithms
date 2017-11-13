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
                myEdges.append((weight, (v, u)))
                heapInsert(u, readRow(u+1), myHeap)  # add all the edges of the vertex we added into heap
                MSTtotal += weight  # add the weight to MST total weight
            elif label[u] != label[v] and label[u] == 1:  # if the vertex 'u' is already in MST
                label[v] = 1  # add 'v' to the MST
                myEdges.append((weight, (v, u)))
                heapInsert(v, readRow(v+1), myHeap)  # add all the edges of the vertex we added into heap
                MSTtotal += weight  # add the weight to MST total weight
    return MSTtotal, myEdges


myEdges = []

# initializing list
myHeap = []
label = [0 for x in range(n)]

# using heapify to convert list into heap
heapq.heapify(myHeap)

# insert the first vertex into the heap with all of its its edges
# i.e. the first row if the adjacency matrix
heapInsert(0, readRow(1), myHeap)

# update label array
label[0] = 1

first_mst = primMST(myHeap, (-1, (-1, -1)))
f = open("output.txt", "w+")
f.write(str(first_mst[0]) + '\n')

#  ------------------------------------------------------------
#  -------------------- FIND THE SECOND MST -------------------
#  ------------------------------------------------------------

min = -1
for bad_edge in first_mst[1]:
    myEdges = []
    # initializing list
    myHeap = []
    label = [0 for x in range(n)]

    # using heapify to convert list into heap
    heapq.heapify(myHeap)

    # insert the first vertex into the heap with all of its its edges
    # i.e. the first row if the adjacency matrix
    heapInsert(0, readRow(1), myHeap)

    # update label array
    label[0] = 1
    second_MST = primMST(myHeap, bad_edge)
    if min == -1 or second_MST[0] < min:
        min = second_MST[0]
        MSTedgesMin = second_MST[1]  # store the edges of the min tree we're gonna keep


f.write(str(min) + '\n')

#  ------------------------------------------------------------
#  -------------------- FIND THE THIRD MST --------------------
#  ------------------------------------------------------------

secondMSTtotal = min
min = -1
for bad_edge in MSTedgesMin:
    myEdges = []
    # initializing list
    myHeap = []
    label = [0 for x in range(n)]

    # using heapify to convert list into heap
    heapq.heapify(myHeap)

    # insert the first vertex into the heap with all of its its edges
    # i.e. the first row if the adjacency matrix
    heapInsert(0, readRow(1), myHeap)

    # update label array
    label[0] = 1
    third_MST = primMST(myHeap, bad_edge)
    if (min == -1 or third_MST[0] < min) and third_MST[0] >= secondMSTtotal:
        min = third_MST[0]
        MSTedgesMin = second_MST[1]  # store the edges of the min tree we're gonna keep


f.write(str(min) + '\n')

exit(0)




