# ESP32 Dog Button

A physical button my dog presses when she needs to go out. An ESP32 running C++ firmware detects the press and sends a push notification to my phone. A small Python server logs each press and shows bathroom-break intervals over time.

**Stack:** C++ (Arduino framework on ESP32) for the firmware, Python with FastAPI for the server, ntfy for notifications.

## How it works

1. **Firmware (`esp32code.cpp`)**
   - Reads a GPIO button (pin 27, internal pull-up) and detects the HIGH-to-LOW falling edge.
   - Debounces with short delays and ignores repeat presses during a 5-minute cooldown, using `millis()` timing.
   - On a valid press, sends two HTTP POSTs over Wi-Fi: one to ntfy for the phone notification, and one to the logging server.
2. **Server (`main.py`, `functions.py`)**
   - FastAPI app that records each press timestamp.
   - Serves a page showing presses and average intervals for today, the last 24 hours, the last 7 days and the last month.

## Hardware

- ESP32 dev board
- Momentary push button wired between GPIO 27 and GND

## Setup

- Firmware: set your Wi-Fi SSID and password and the server and ntfy URLs in `esp32code.cpp`, then flash it with the Arduino IDE or PlatformIO.
- Server: `pip install fastapi uvicorn`, then `uvicorn main:app --host 0.0.0.0`.
