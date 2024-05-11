def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key

arr = [3,7,3,8,9,44,17,99,2,34]
insertionSort(arr)
print(arr)
