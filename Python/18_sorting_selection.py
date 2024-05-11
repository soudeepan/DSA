def selectionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]

arr = [3,7,3,8,9,44,17,99,2,34]
selectionSort(arr)
print(arr)
