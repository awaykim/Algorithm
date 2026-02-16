N = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]

def find_place(n: int):
  left = 0
  right = len(lis) - 1
  while left <= right:
    mid = (left + right) // 2
    if lis[mid] < n:
      left = mid + 1
    elif lis[mid] > n:
      right = mid - 1
    else:
      return mid
  return left

for i in range(N):
  if lis[-1] < arr[i]:
    lis.append(arr[i])
  elif lis[-1] > arr[i]:
      place = find_place(arr[i])
      lis[place] = arr[i]

print(len(lis))