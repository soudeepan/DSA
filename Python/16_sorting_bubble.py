
def bubbleSort(arr):
    n = len(arr)-1
    for i in range(n-1):
        for j in range(n-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [3,7,3,8,9,44,17,99,2,34]
bubbleSort(arr)
print(arr)
