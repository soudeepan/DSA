def heapify(arr,n,i):
    largest = i
    l,r = i*2+1,i*2+2

    if l < n and arr[l] > arr[i]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

arr = [3,7,3,8,9,44,17,99,2,34]
heapSort(arr)
print(arr)