#include <WiFi.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT22
#define MQ4_PIN 34
#define MQ135_PIN 35
#define BUZZER_PIN 26

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  pinMode(BUZZER_PIN, OUTPUT);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  int methaneValue = analogRead(MQ4_PIN);
  int airQuality = analogRead(MQ135_PIN);

  Serial.println("----- SENSOR DATA -----");
  Serial.print("Temperature: ");
  Serial.println(temperature);

  Serial.print("Humidity: ");
  Serial.println(humidity);

  Serial.print("Methane Level: ");
  Serial.println(methaneValue);

  Serial.print("Air Quality: ");
  Serial.println(airQuality);

  if (methaneValue > 500) {
    digitalWrite(BUZZER_PIN, HIGH);
    Serial.println("WARNING: High Methane Level!");
  } else {
    digitalWrite(BUZZER_PIN, LOW);
  }

  delay(5000);
}