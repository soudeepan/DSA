
def countingSort(arr,exp):

    n = len(arr)
    output = [0]*n
    count = [0]*10

    for i in range(0,n):
        index = arr[i] // exp
        count[index % 10] += 1 

    for i in range(1,10):
        count[i] += count[i-1]

    for i in range(n-1,-1,-1):
        index = arr[i] // exp
        output[count[index % 10]-1] = arr[i]
        count[index % 10] -= 1

    for i in range(0,n):
        arr[i] = output[i]


def radixSort(arr):
    
    maxn = max(arr)

    exp = 1
    while maxn // exp >= 1:
        countingSort(arr,exp)
        exp*=10


arr = [3,7,3,8,9,44,17,99,2,34]
radixSort(arr)
print(arr)