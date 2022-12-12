#https://programmers.co.kr/learn/courses/30/lessons/42579
from collections import defaultdict

def solution(genres, plays):
    play_count_by_genres = defaultdict(int)
    songs_in_genre = defaultdict(list)

    song_id = 0
    for genre, play in zip(genres, plays):
        play_count_by_genres[genre] += play
        songs_in_genre[genre].append((-play, song_id))
        song_id += 1


    genre_in_order = sorted(play_count_by_genres.keys(),
                            key= lambda x: -play_count_by_genres[x])
    answer = []

    for genre in genre_in_order:
        answer.extend([i[1] for i in sorted(songs_in_genre[genre])[:2]])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))