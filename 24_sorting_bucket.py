def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key

def bucketSort(arr):

    n = len(arr)

    buckets = [[] for _ in range(n)]

    for ele in arr:
        bi = int(n*ele)
        buckets[bi].append(ele)

    
    for bucket in buckets:
        insertionSort(bucket)

    index = 0
    for bucket in buckets:
        for ele in bucket:
            arr[index] = ele
            index+=1

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucketSort(arr)
print(arr)