t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    # order = []
    # i = 0
    # while len(order) < n:
    #     if i >= n: i = 0
    #     if docs[i] == max(docs): 
    #         docs[i] = 0
    #         order.append(i)
    #     i += 1
    # print(order.index(m) + 1)
    cnt = 0
    i = 0
    while True:
        if i >= n: i = 0
        if docs[i] == max(docs):
            cnt += 1
            if i == m: 
                print(cnt)
                break
            docs[i] = 0
        i += 1