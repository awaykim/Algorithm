num1 = int(input())
num2 = int(input())

third = num1 * int(str(num2)[2])
forth = num1 * int(str(num2)[1])
fifth = num1 * int(str(num2)[0])
sixth = third + forth*10 + fifth*100

print(third)
print(forth)
print(fifth)
print(sixth)
