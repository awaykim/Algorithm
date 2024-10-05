def solution(genres, plays):
    answer = []
    # dictionary 선언 
    songs = {}
    gen_counts = {}
    # 장르 별로 모으기
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in gen_counts:
            gen_counts[genre] = 0
            songs[genre] = []
        gen_counts[genre] += play
        songs[genre].append((play, i))
    # 장르 정렬 
    sorted_gen = sorted(gen_counts.keys(), key=lambda x: -gen_counts[x])
    # 장르 내에서 정렬
    for genre in songs:
        songs[genre].sort(key=lambda x: (-x[0], x[1]))
    # 최상위 2개까지만 수록
    for genre in sorted_gen:
        answer.append(songs[genre][0][1])
        if len(songs[genre]) > 1:
            answer.append(songs[genre][1][1])
    return answer