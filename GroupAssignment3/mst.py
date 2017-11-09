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


# T - set of MST vertices
# V - any vertex
# H - empty heap

Tone = 0
lastAdded = 0
# initializing list
myHeap = []
label = [0 for x in range(n)]
print(label)
# using heapify to convert list into heap
heapq.heapify(myHeap)

heapInsert(0, adjMatrix[0], myHeap)
label[0] = 1
print(myHeap)

while len(myHeap) > 0:  # while heap is not empty
    (weight, (v, u)) = heapq.heappop(myHeap)
    if label[u] != label[v] and label[v] == 1:
        label[u] = 1
        lastAdded = (weight, u)
        heapInsert(u, adjMatrix[u], myHeap)
        Tone += weight
    elif label[u] != label[v] and label[u] == 1:
        label[v] = 1
        lastAdded = (weight, v)
        heapInsert(v, adjMatrix[v], myHeap)
        Tone += weight
    print(Tone)
    print(myHeap)


print(list(myHeap))
print(list(myHeap))
exit(0)




