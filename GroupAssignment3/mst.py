#!/usr/bin/python

# importing "heapq" to implement heap queue
import heapq



# READ input.txt
# 1st line 0 < n < 30
# rest lines n lines of n values delim ',' 0 < n < 30
with open('input.txt', 'r') as f:
    n = int(f.readline())
    adjMatrix = [line.strip('\n').split(',') for line in f]
    adjMatrix = [[int(y) for y in x] for x in adjMatrix]
    f.close()


def heapInsert(v, arr, heap):
    for i in range(0, len(arr)):
        if i != v:
            heapq.heappush(heap, (arr[i], (v, i)))



firstMSTtotal = 0
lastAdded = 0
# initializing list
myHeap = []
label = [0 for x in range(n)]
# using heapify to convert list into heap
heapq.heapify(myHeap)

# insert the first vertex into the heap with all of its its edges
# i.e. the first row if the adjacency matrix
heapInsert(0, adjMatrix[0], myHeap)

# update label array
label[0] = 1


# while heap is not empty
while len(myHeap) > 0:
    (weight, (v, u)) = heapq.heappop(myHeap)  # pop the minimum weight edge (root) from heap

    #  look at both vertices of the edge we just pulled from the heap
    if label[u] != label[v] and label[v] == 1:  # if the vertex 'v' is already in MST
        label[u] = 1  # add 'u' to the MST
        lastAdded = (weight, u)  # update the lastAdded variable
        heapInsert(u, adjMatrix[u], myHeap)  # add all the edges of the vertex we added into heap
        firstMSTtotal += weight  # add the weight to MST total weight
    elif label[u] != label[v] and label[u] == 1:  # if the vertex 'u' is already in MST
        label[v] = 1  # add 'v' to the MST
        lastAdded = (weight, v)  # update the lastAdded variable
        heapInsert(v, adjMatrix[v], myHeap)  # add all the edges of the vertex we added into heap
        firstMSTtotal += weight  # add the weight to MST total weight

f = open("output.txt", "w+")
f.write(str(firstMSTtotal))

exit(0)




