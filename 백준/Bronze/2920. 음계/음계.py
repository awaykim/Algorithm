
playing = list(map(int, input().split()))
if playing[0] < playing[1]: flag = True
else: flag = False
for i in range(1,len(playing)-1):
    if playing[i] < playing[i+1]: # ascending
        if not flag: 
            print("mixed")
            exit()
    else:
        if flag:
            print("mixed")
            exit()
if flag: print("ascending")
else: print("descending")