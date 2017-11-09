#!/usr/bin/python

# importing "heapq" to implement heap queue
import heapq


def Jurnik(G, w):

    # T - set of MST vertices
    # V - any vertex
    # H - empty heap

    # Insert all v-edges into H
    # importing "heapq" to implement heap queue
    import heapq

    # initializing list
    li = [5, 7, 9, 1, 3]

    # using heapify to convert list into heap
    heapq.heapify(li)

    print(list(li))


    # using heappush() to push elements into heap
    # pushes 4
    heapq.heappush(li, 4)

    # printing modified heap
    print("The modified heap after push is : ", end="")
    print(list(li))

    # using heappop() to pop smallest element
    print("The popped and smallest element is : ", end="")
    print(heapq.heappop(li))

Jurnik(2, 2)