expr = input()
arr = []
ans = 0
for e in expr:
  try:
    if 0 <= int(e) <= 9:
      if arr and int(arr[-1]):
        arr[-1] = f"{arr[-1]}{e}"
        continue
  except: pass
  arr.append(e)
minus = False

for a in arr:
  try:
    number = int(a)
    if minus:
      ans -= number
    else:
      ans += number
  except:
    if a == "+": continue
    else: minus = True

print(ans)