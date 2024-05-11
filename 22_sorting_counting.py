def countingSort(arr):

    n = len(arr)
    output = [0]*n
    count = [0]*10

    for i in range(0,n):
        index = arr[i]
        count[index % 10] += 1 

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n-1,-1,-1):
        index = arr[i]
        output[count[index % 10]-1] = arr[i]
        count[index % 10] -= 1

    for i in range(0,n):
        arr[i] = output[i]


arr = [3,7,3,1,6,3,6,8,3]
countingSort(arr)
print(arr)