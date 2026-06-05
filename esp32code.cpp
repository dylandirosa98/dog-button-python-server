#include <WiFi.h>
#include <HTTPClient.h>
#include <WiFiClientSecure.h>

const int buttonPin = 27;

const char* ssid = "MOTO4B50";
const char* password = "w3pfp4wyy9";

const char* ntfyUrl = "https://ntfy.sh/nox_bathroom";
const char* serverUrl = "https://nox-button.duckdns.org/times";

const unsigned long cooldown = 300000; // 5 minutes
unsigned long lastPressTime = 0;
bool firstPress = true;

int lastButtonState = HIGH;

void setup() {
  Serial.begin(115200);

  pinMode(buttonPin, INPUT_PULLUP);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

void loop() {
  int buttonState = digitalRead(buttonPin);
  unsigned long currentTime = millis();

  // Detect button press (HIGH -> LOW)
  if (lastButtonState == HIGH && buttonState == LOW) {
    if (firstPress || currentTime - lastPressTime >= cooldown) {
      Serial.println("Button pressed!");

      sendNtfyNotification();
      sendToServer();

      lastPressTime = currentTime;
      firstPress = false;
    } else {
      Serial.println("Cooldown active - ignoring press");
    }

    delay(300);
  }

  lastButtonState = buttonState;
  delay(50);
}

void sendNtfyNotification() {
  if (WiFi.status() == WL_CONNECTED) {
    WiFiClientSecure client;
    client.setInsecure();

    HTTPClient http;
    http.begin(client, ntfyUrl);

    http.addHeader("Content-Type", "text/plain");
    http.addHeader("Title", "Dog Button");
    http.addHeader("Priority", "high");
    http.addHeader("Tags", "dog");

    int responseCode = http.POST("Nox has to go to the bathroom");

    Serial.print("ntfy response code: ");
    Serial.println(responseCode);

    http.end();
  }
}

void sendToServer() {
  if (WiFi.status() == WL_CONNECTED) {
    WiFiClientSecure client;
    client.setInsecure();

    HTTPClient http;
    http.begin(client, serverUrl);

    int responseCode = http.POST("");

    Serial.print("server response code: ");
    Serial.println(responseCode);

    http.end();
  }
}
