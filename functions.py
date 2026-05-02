from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


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


def last_24_hours(times, time_intervals):
    new_times = times.copy()
    new_time_intervals = time_intervals.copy()
    last_24_times = []
    last_24_intervals = []
    now = datetime.now(ZoneInfo("US/Eastern"))
    for i in range(len(new_times) - 1, -1, -1):
        if now - new_times[i] > timedelta(hours=24):
            break
        else:
            last_24_times.insert(0, new_times[i])
    for i in range(len(last_24_times)):
        last_24_intervals.insert(0, new_time_intervals[-i - 1])
    avg = avg_time_interval(last_24_intervals)
    return [last_24_times, last_24_intervals, avg]


def last_7_days(times, time_intervals):
    new_times = times.copy()
    new_time_intervals = time_intervals.copy()
    last_7_times = []
    last_7_intervals = []
    now = datetime.now(ZoneInfo("US/Eastern"))
    for i in range(len(new_times) - 1, -1, -1):
        if now - new_times[i] > timedelta(days=7):
            break
        else:
            last_7_times.insert(0, new_times[i])
    for i in range(len(last_7_times)):
        last_7_intervals.insert(0, new_time_intervals[-i - 1])
    avg = avg_time_interval(last_7_intervals)
    return [last_7_times, last_7_intervals, avg]


def last_month(times, time_intervals):
    new_times = times.copy()
    new_time_intervals = time_intervals.copy()
    last_month_times = []
    last_month_intervals = []
    now = datetime.now(ZoneInfo("US/Eastern"))
    for i in range(len(new_times) - 1, -1, -1):
        if now - new_times[i] > timedelta(days=30):
            break
        else:
            last_month_times.insert(0, new_times[i])
    for i in range(len(last_month_times)):
        last_month_intervals.insert(0, new_time_intervals[-i - 1])
    avg = avg_time_interval(last_month_intervals)
    return [last_month_times, last_month_intervals, avg]


def today(times, time_intervals):
    new_times = times.copy()
    new_time_intervals = time_intervals.copy()
    today_times = []
    today_intervals = []
    now = datetime.now(ZoneInfo("US/Eastern"))
    start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    for i in range(len(new_times) - 1, -1, -1):
        if new_times[i] < start_of_today:
            break
        else:
            today_times.insert(0, new_times[i])
    for i in range(len(today_times)):
        today_intervals.insert(0, new_time_intervals[-i - 1])
    avg = avg_time_interval(today_intervals)
    return [today_times, today_intervals, avg]
