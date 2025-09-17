def solution(cacheSize, cities):
    HIT_TIME = 1
    MISS_TIME = 5
    cache = [] 
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache: 
            answer += HIT_TIME
            cache.remove(city)
            cache.append(city)
        else: 
            answer += MISS_TIME
            cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)
    return answer