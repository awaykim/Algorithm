import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pokemon_num = {}
pokemon_name = {}
for i in range(n):
    pokemon = input().rstrip()
    pokemon_num[i] = pokemon
    pokemon_name[pokemon] = i
for _ in range(m):
    p = input().rstrip()
    if p.isdigit():
        print(pokemon_num[int(p)-1])
    else:
        print(pokemon_name[p]+1)