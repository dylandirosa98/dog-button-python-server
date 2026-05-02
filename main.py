from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

from fastapi import FastAPI

from functions import add_time_interval, avg_time_interval

app = FastAPI()
time_intervals = []
times = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/times")
def create_time():
    time = datetime.now(ZoneInfo("US/Eastern"))
    add_time_interval(time, times, time_intervals)
    avg = avg_time_interval(time_intervals)
    return times, time_intervals, avg
