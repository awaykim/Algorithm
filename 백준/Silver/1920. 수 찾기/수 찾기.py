# 1920 수 찾기
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
num = list(map(int, input().split()))

for i in num:
    flag = 0
    start, end = 0, n-1
    while start <=  end:
        mid = (start + end) // 2
        if arr[mid] == i: 
            flag = 1
            break
        elif arr[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    print(flag)