def getAlternates(arr):
    for i in range(0, len(arr), 2):
        print(arr[i], end=" ")

arr = list(map(int, input().split()))
getAlternates(arr)
