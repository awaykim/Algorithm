def is_prime_num_until(n):
    check_prime = [True] * (n + 1) # 특정 수가 소수인지 아닌지 확인하는 배열
    for i in range(n + 1):
      if i < 2: 
        check_prime[i] = False
        continue

      if check_prime[i] == True: # 특정 수가 소수인 경우
        j = 2
        while (i * j) <= n:
            check_prime[i*j] = False # i의 배수의 값을 False로 지워준다.
            j += 1

    primes = []
    for i in range(len(check_prime)):
      if check_prime[i]: 
        primes.append(i)
    
    return primes

N = int(input())
primes = is_prime_num_until(N)
ans = 0
i = 0
j = 0
tmp = primes[0] if primes else 0
while i < len(primes):
  if tmp < N:
    j+=1
    if j == len(primes):
      break
    tmp = tmp + primes[j]
  else:
    if tmp == N:
      ans+=1
    tmp -= primes[i]
    i+=1

print(ans)
