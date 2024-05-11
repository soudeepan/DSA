
# linear search

def linearSearch(arr,key):
    for i,ele in enumerate(arr):
        if ele == key:
            return i

# Binary Search

def binarySearch(arr,key):
    low = 0 
    high = len(arr)-1
    mid = None

    while low <= high:

        mid = int((low + high)/2)
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        else:
            return mid
        
    return -1
        

# Interpollation Search

def interpollationSearch(arr,high,low,key):

    while(low <= high and key >= arr[low] and key <= arr[high]):
        
        probe = int((key - arr[low])/(arr[high] - arr[low])*(high-low))

        if arr[probe] == key:
            return probe
        elif arr[probe] < key:
            return interpollationSearch(arr,probe+1,high)
        else:
            return interpollationSearch(arr,low,probe-1)

    return -1
    


arr = [1,2,3,4,5,6,7,8,9]

print(linearSearch(arr,3))
print(binarySearch(arr,3))
print(interpollationSearch(arr,len(arr)-1,0,3))