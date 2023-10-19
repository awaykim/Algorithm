n, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers = sorted(numbers, reverse=True)
print(sum(numbers[:k]) - sum(range(k)))