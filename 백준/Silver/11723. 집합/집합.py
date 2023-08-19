# 11723
import sys
m = int(sys.stdin.readline())
s = set()
twenty = set()
for i in range(1, 21):
    twenty.add(i)
for _ in range(m):
    cmd = list(map(str, sys.stdin.readline().split()))
    if cmd[0] == 'add': 
        s.add(int(cmd[1]))
    elif cmd[0] == 'remove': 
        if int(cmd[1]) in s: s.remove(int(cmd[1]))
    elif cmd[0] == 'check': 
        if int(cmd[1]) in s: print(1)
        else: print(0)
    elif cmd[0] == 'toggle': 
        if int(cmd[1]) in s: s.remove(int(cmd[1]))
        else: s.add(int(cmd[1]))
    elif cmd[0] == 'all': 
        s.update(twenty)
    else: 
        s = set()
    
   
    