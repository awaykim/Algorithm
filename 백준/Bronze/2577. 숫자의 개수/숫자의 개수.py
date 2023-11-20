a = int(input())
b = int(input())
c = int(input())
abc = a * b * c
for i in range(10):
    print(str(abc).count(str(i)))