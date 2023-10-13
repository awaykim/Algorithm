n = int(input())
drinks = list(map(float, input().split()))
drinks.sort()
new_drink = drinks[-1]
for i in range(len(drinks)-1):
    new_drink +=  drinks[i] / 2 
print(new_drink)