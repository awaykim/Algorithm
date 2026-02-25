N = int(input())
nums = list(map(int, input().split()))

nums.sort()
ans = 10000000000
x = y = 0
left = 0
right = N-1
while left < right:
  a = nums[left]
  b = nums[right]
  if a+b>0:
    right -= 1
  else:
    left += 1 
  if abs(a+b) < abs(ans):
    ans = a+b
    x = a
    y = b

print(x, y)