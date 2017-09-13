import heapq

def heapsort(iterable):
    print(iterable)
    h = []
    for value in iterable: heapq.heappush(h, value)
    print(h)
    return [heapq.heappop(h) for i in range(len(h))]

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

