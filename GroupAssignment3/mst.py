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

myMST = [[0 for y in x] for x in adjMatrix]
MSTedges = []
print(myMST)
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
        myMST[u][v] = weight
        myMST[v][u] = weight
        MSTedges.append((weight, (v, u)))
        lastAdded = (weight, u)  # update the lastAdded variable
        heapInsert(u, adjMatrix[u], myHeap)  # add all the edges of the vertex we added into heap
        firstMSTtotal += weight  # add the weight to MST total weight
    elif label[u] != label[v] and label[u] == 1:  # if the vertex 'u' is already in MST
        label[v] = 1  # add 'v' to the MST
        myMST[u][v] = weight
        myMST[v][u] = weight
        MSTedges.append((weight, (v, u)))
        lastAdded = (weight, v)  # update the lastAdded variable
        heapInsert(v, adjMatrix[v], myHeap)  # add all the edges of the vertex we added into heap
        firstMSTtotal += weight  # add the weight to MST total weight
print(myMST)
print(MSTedges)
f = open("output.txt", "w+")
f.write(str(firstMSTtotal) + '\n')

secondMSTtotal = 0
lastAdded = 0


print(MSTedges)
print(myHeap)
min = -1
MSTedgesMin = []
print("-------------BEGINNING---------------")
for edge in MSTedges:
    myMST = [[0 for y in x] for x in adjMatrix]
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
    # find second by finding the minimum MST with an edge of MSTone excluded


    MSTtwoedges = []

    secondMSTtotal = 0
    print("EDGE")
    print(edge)
    (w, (v1, v2)) = edge
    while len(myHeap) > 0:
        (weight, (v, u)) = heapq.heappop(myHeap)  # pop the minimum weight edge (root) from heap
        print((weight, (v, u)))
        if (v1 == v and v2 == u) or (v1 == u and v2 == v):
            print("bad edge")
        else:
            #  look at both vertices of the edge we just pulled from the heap
            if label[u] != label[v] and label[v] == 1:  # if the vertex 'v' is already in MST
                label[u] = 1  # add 'u' to the MST
                myMST[u][v] = weight
                myMST[v][u] = weight
                MSTtwoedges.append((weight, (v, u)))
                lastAdded = (weight, u)  # update the lastAdded variable
                heapInsert(u, adjMatrix[u], myHeap)  # add all the edges of the vertex we added into heap
                secondMSTtotal += weight  # add the weight to MST total weight
            elif label[u] != label[v] and label[u] == 1:  # if the vertex 'u' is already in MST
                label[v] = 1  # add 'v' to the MST
                myMST[u][v] = weight
                myMST[v][u] = weight
                MSTtwoedges.append((weight, (v, u)))
                lastAdded = (weight, v)  # update the lastAdded variable
                heapInsert(v, adjMatrix[v], myHeap)  # add all the edges of the vertex we added into heap
                secondMSTtotal += weight  # add the weight to MST total weight

    if min == -1 or secondMSTtotal < min:
        print(secondMSTtotal)
        min = secondMSTtotal
        MSTedgesMin = MSTtwoedges

f.write(str(min) + '\n')
secondMSTtotal = min
print(MSTedgesMin)
min = -1

print("-------------THIRD---------------")

for edge in MSTedgesMin:
    myMST = [[0 for y in x] for x in adjMatrix]
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
    # find second by finding the minimum MST with an edge of MSTone excluded


    MSTthreeedges = []
    thirdMSTtotal = 0
    (w, (v1, v2)) = edge
    while len(myHeap) > 0:
        (weight, (v, u)) = heapq.heappop(myHeap)  # pop the minimum weight edge (root) from heap
        if (v1 == v and v2 == u) or (v1 == u and v2 == v):
            miaa = 0
        else:
            #  look at both vertices of the edge we just pulled from the heap
            if label[u] != label[v] and label[v] == 1:  # if the vertex 'v' is already in MST
                label[u] = 1  # add 'u' to the MST
                myMST[u][v] = weight
                myMST[v][u] = weight
                MSTthreeedges.append((weight, (v, u)))
                lastAdded = (weight, u)  # update the lastAdded variable
                heapInsert(u, adjMatrix[u], myHeap)  # add all the edges of the vertex we added into heap
                thirdMSTtotal += weight  # add the weight to MST total weight
            elif label[u] != label[v] and label[u] == 1:  # if the vertex 'u' is already in MST
                label[v] = 1  # add 'v' to the MST
                myMST[u][v] = weight
                myMST[v][u] = weight
                MSTthreeedges.append((weight, (v, u)))
                lastAdded = (weight, v)  # update the lastAdded variable
                heapInsert(v, adjMatrix[v], myHeap)  # add all the edges of the vertex we added into heap
                thirdMSTtotal += weight  # add the weight to MST total weight

    print(thirdMSTtotal)
    if (min == -1 or thirdMSTtotal < min) and thirdMSTtotal >= secondMSTtotal:
        min = thirdMSTtotal

f.write(str(min) + '\n')

exit(0)




