import sys
s = list(map(str, sys.stdin.readline().strip()))
t = list(map(str, sys.stdin.readline().strip()))
def string_dfs(string):
    if not string: return
    if string == s: 
        print(1)
        exit()
    if string[0] == 'B':
        string.reverse()
        string.pop()
        string_dfs(string)
        string.append('B')
        string.reverse()
    if string[-1] == 'A':
        string.pop()
        string_dfs(string)
        string.append('A')   
    return
string_dfs(t)
print(0)     