def partition(arr,low,high):
    pivot = arr[high]

    i =low-1

    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1
    

def quickSort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)

        quickSort(arr,low,pivot-1)
        quickSort(arr,pivot+2,high)


arr = [3,7,3,8,9,44,17,99,2,34]
quickSort(arr,0,len(arr)-1)
print(arr)
