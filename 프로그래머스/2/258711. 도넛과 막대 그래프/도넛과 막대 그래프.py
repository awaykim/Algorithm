def solution(edges):
    answer = [0 for _ in range(4)]
    graph_cnt = 0
    # key - value [in, out]
    graph = dict()
    for edge in edges:
        s, e = edge[0], edge[1]
        if s in graph: 
            graph[s][1] += 1
        else:
            graph[s] = [0,1]
        if e in graph:
            graph[e][0] += 1
        else:
            graph[e] = [1,0]
    for node in graph:
        in_cnt, out_cnt = graph[node][0], graph[node][1]
        if in_cnt == 0 and out_cnt > 1:
            answer[0] = node
            graph_cnt = out_cnt
        elif out_cnt == 0:
            answer[2] += 1
        elif out_cnt == 2:
            answer[3] += 1
    answer[1] = graph_cnt - answer[2] - answer[3]
    
    
    return answer