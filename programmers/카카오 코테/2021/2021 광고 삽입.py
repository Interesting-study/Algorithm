def convert_to_secs(times):
    times = map(int, times.split(":"))
    result = 0

    for t, sec in zip(times, [3600, 60, 1]):
        result += t * sec

    return result

def convert_to_string(times):
    sec = times % 60
    times //= 60
    minutes = times % 60
    times //= 60
    hour = times

    return '{:02d}:{:02d}:{:02d}'.format(hour, minutes, sec)

def solution(play_time, adv_time, logs):

    if play_time == adv_time:
        return "00:00:00"

    play_sec = convert_to_secs(play_time)
    adv_sec = convert_to_secs(adv_time)

    #100시간 미만이므로
    cum_played = [0 for _ in range(360001)]

    for log in logs:
        log = log.split("-")

        cum_played[convert_to_secs(log[0])] += 1
        cum_played[convert_to_secs(log[1])] -= 1

    #구간별로 재생횟수를 구하기
    for idx in range(1, play_sec + 1):
        cum_played[idx] += cum_played[idx - 1]

    #누적 재생횟수 구하기
    for idx in range(1, play_sec + 1):
        cum_played[idx] += cum_played[idx - 1]

    max_sum_time = 0

    #00:00:00 초를 시작으로 잡는다
    max_sum_played = cum_played[adv_sec]
    for start_time in range(1, play_sec):
        end_time = (start_time + adv_sec) if start_time + adv_sec < play_sec else play_sec
        sum_played = cum_played[end_time] - cum_played[start_time]

        if max_sum_played < sum_played:
            max_sum_played = sum_played
            max_sum_time = start_time + 1

    return convert_to_string(max_sum_time)



solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])