from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from functions import (
    add_time_interval,
    avg_time_interval,
    last_7_days,
    last_24_hours,
    last_month,
    today,
)

app = FastAPI()
time_intervals = []
times = []
avg = timedelta(0)


@app.get("/", response_class=HTMLResponse)
def home():
    today_times = today(times, time_intervals)[0]
    today_intervals = today(times, time_intervals)[1]
    today_avg = today(times, time_intervals)[2]
    last_24_times = last_24_hours(times, time_intervals)[0]
    last_24_intervals = last_24_hours(times, time_intervals)[1]
    last_24_avg = last_24_hours(times, time_intervals)[2]
    last_7_times = last_7_days(times, time_intervals)[0]
    last_7_intervals = last_7_days(times, time_intervals)[1]
    last_7_avg = last_7_days(times, time_intervals)[2]
    last_month_times = last_month(times, time_intervals)[0]
    last_month_intervals = last_month(times, time_intervals)[1]
    last_month_avg = last_month(times, time_intervals)[2]
    return f"""
    <html>
        <head>
            <title>Dog Button Dashboard</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">

            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 16px;
                    background: #f5f5f5;
                    color: #222;
                }}

                h1 {{
                    font-size: 28px;
                    margin-bottom: 20px;
                    text-align: center;
                }}

                h2 {{
                    font-size: 22px;
                    margin: 0 0 10px 0;
                }}

                h3 {{
                    font-size: 16px;
                    margin-top: 16px;
                }}

                .section {{
                    background: white;
                    padding: 16px;
                    margin-bottom: 18px;
                    border-radius: 12px;
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
                }}

                .stat {{
                    font-size: 16px;
                    margin: 8px 0;
                }}

                details {{
                    margin-top: 10px;
                    background: #fafafa;
                    padding: 10px;
                    border-radius: 8px;
                    border: 1px solid #ddd;
                }}

                summary {{
                    font-weight: bold;
                    cursor: pointer;
                }}

                ul {{
                    margin-top: 10px;
                    padding-left: 18px;
                    overflow-wrap: break-word;
                    word-break: break-word;
                }}

                li {{
                    margin-bottom: 6px;
                }}
            </style>
        </head>

        <body>
            <h1>Dog Button Dashboard</h1>

            <!-- TODAY -->
            <div class="section">
                <h2>Today</h2>
                <p class="stat">Total presses: {len(today_times)}</p>
                <p class="stat">Average interval no overnight: {today_avg}</p>

                <details>
                    <summary>Press Times</summary>
                    <ul>
                        {today_times}
                    </ul>
                </details>

                <details>
                    <summary>Intervals</summary>
                    <ul>
                        {today_intervals}
                    </ul>
                </details>
            </div>

            <!-- LAST 24 HOURS -->
            <div class="section">
                <h2>Last 24 Hours</h2>
                <p class="stat">Total presses: {len(last_24_times)}</p>
                <p class="stat">Average interval no overnight: {last_24_avg}</p>

                <details>
                    <summary>Press Times</summary>
                    <ul>
                        {last_24_times}
                    </ul>
                </details>

                <details>
                    <summary>Intervals</summary>
                    <ul>
                        {last_24_intervals}
                    </ul>
                </details>
            </div>

            <!-- LAST 7 DAYS -->
            <div class="section">
                <h2>Last 7 Days</h2>
                <p class="stat">Total presses: {len(last_7_times)}</p>
                <p class="stat">Average interval no overnight: {last_7_avg}</p>

                <details>
                    <summary>Press Times</summary>
                    <ul>
                        {last_7_times}
                    </ul>
                </details>

                <details>
                    <summary>Intervals</summary>
                    <ul>
                        {last_7_intervals}
                    </ul>
                </details>
            </div>

            <!-- LAST 30 DAYS -->
            <div class="section">
                <h2>Last 30 Days</h2>
                <p class="stat">Total presses: {len(last_month_times)}</p>
                <p class="stat">Average interval no overnight: {last_month_avg}</p>

                <details>
                    <summary>Press Times</summary>
                    <ul>
                        {last_month_times}
                    </ul>
                </details>

                <details>
                    <summary>Intervals</summary>
                    <ul>
                        {last_month_intervals}
                    </ul>
                </details>
            </div>

            <!-- ALL TIME -->
            <div class="section">
                <h2>All Time</h2>
                <p class="stat">Total presses: {len(times)}</p>
                <p class="stat">Average interval no overnight: {avg_time_interval(time_intervals)}</p>

                <details>
                    <summary>Press Times</summary>
                    <ul>
                        {times}
                    </ul>
                </details>

                <details>
                    <summary>Intervals</summary>
                    <ul>
                        {time_intervals}
                    </ul>
                </details>
            </div>

        </body>
    </html>
    """


@app.post("/times")
def create_time():
    time = datetime.now(ZoneInfo("US/Eastern"))
    add_time_interval(time, times, time_intervals)
    return {"status": "ok"}
