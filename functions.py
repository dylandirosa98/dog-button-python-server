from datetime import timedelta


def add_time_interval(time, times, time_intervals):
    times.append(time)
    if len(times) >= 2:
        interval = times[-1] - times[-2]
        time_intervals.append(interval)


def avg_time_interval(time_intervals):
    new_intervals = []
    time = timedelta(0)
    for time_interval in time_intervals:
        if time_interval < timedelta(hours=10):
            new_intervals.append(time_interval)
            time += time_interval
    if len(new_intervals) > 0:
        return time / len(new_intervals)
    else:
        return "no intervals"
