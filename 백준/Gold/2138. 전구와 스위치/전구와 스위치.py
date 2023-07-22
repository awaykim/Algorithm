N = int(input())
initState = list(map(int, input())) # 0 ~ n-1 만큼
finState = list(map(int, input()))
array = initState.copy()

def switch(index):
    if 0 < index < N - 1:
        for i in range(index-1,index+2): 
            initState[i] = 1 - initState[i]
    elif index == 0: 
        for i in range(0,index+2):
            initState[i] = 1 - initState[i]
    else: 
        for i in range(index-1,index+1):
            initState[i] = 1 - initState[i]
    return 


switch(0)
count_on = 1
for i in range(N-1):
    if initState[i] != finState[i]:
        switch(i+1)
        count_on = count_on + 1
 
if initState == finState:
    on_flag = True
else: 
    on_flag = False


initState = array.copy()


count_off = 0
for i in range(N-1):
    if initState[i] != finState[i]:
        switch(i+1)
        count_off = count_off + 1


if initState == finState:
    off_flag = True
else: 
    off_flag = False

if on_flag and off_flag:
    print(min(count_on, count_off))
elif on_flag: print(count_on)
elif off_flag: print(count_off)
else: print(-1)

