n, k = map(int, input().split())
temps = list(map(int, input().split()))
MIN_VALUE = -9999

def two_pointers(arr, bound):
    start = 0
    val = MIN_VALUE
    for i in range(len(arr)-bound+1):
        start = i
        tmp = arr[start]
        for j in range(1,bound):
            tmp = tmp + arr[start+j]
        val = max(tmp, val)
    return val


print(two_pointers(temps, k))