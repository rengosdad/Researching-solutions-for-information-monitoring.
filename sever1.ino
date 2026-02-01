#include <WiFi.h>
#include <WiFiUdp.h>
#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include <DHT.h>

// ====== Cấu hình WiFi (Kết nối vào WiFi nhà để ra Internet) ======
const char* STATION_SSID = "VNPT_Hai";
const char* STATION_PASS = "khongcho";

// ====== UDP (Nhận lệnh từ ESP8266) ======
WiFiUDP udp;
const int UDP_PORT = 4210;

// ====== TFT Pins ======
#define TFT_CS     16
#define TFT_DC     17
#define TFT_RST    5
#define TFT_MOSI   18
#define TFT_SCLK   23

// ====== DHT Sensor ======
#define DHTPIN 13
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// ====== LED Pins ======
#define LED1 25
#define LED2 26
#define LED3 32
#define LED4 33
#define LED5 14 // LED báo trạng thái AI/Hệ thống
#define LED6 27

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);
WiFiServer server(80);

// Biến lưu dữ liệu cảm biến
float currentTemp = 0;
float currentHum = 0;

void setup() {
  Serial.begin(115200);
  dht.begin();

  // Khởi tạo TFT
  SPI.begin(TFT_SCLK, -1, TFT_MOSI, TFT_CS);
  tft.initR(INITR_BLACKTAB);
  tft.setRotation(1);
  tft.fillScreen(ST77XX_BLACK);
  
  // Khởi tạo LED
  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT); pinMode(LED4, OUTPUT);
  pinMode(LED5, OUTPUT); pinMode(LED6, OUTPUT);
  pinMode(LED6, INPUT_PULLUP);
  // Kết nối WiFi
  tft.setCursor(10, 10);
  tft.setTextColor(ST77XX_WHITE);
  tft.println("Connecting WiFi...");
  
  WiFi.begin(STATION_SSID, STATION_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected!");
  tft.fillScreen(ST77XX_BLACK);
  tft.setCursor(10, 10);
  tft.setTextColor(ST77XX_GREEN);
  tft.println("Online Mode");
  tft.setCursor(10, 30);
  tft.setTextSize(1);
  tft.print("IP: "); 
  tft.println(WiFi.localIP()); // In IP ra màn hình để nhập vào Python

  server.begin();
  udp.begin(UDP_PORT);
}

void loop() {
  // Đọc cảm biến mỗi 2 giây
  static unsigned long lastDHTUpdate = 0;
  if (millis() - lastDHTUpdate >= 2000) {
    lastDHTUpdate = millis();
    float t = dht.readTemperature();
    float h = dht.readHumidity();
    
    if (!isnan(t) && !isnan(h)) {
      currentTemp = t;
      currentHum = h;
      updateDisplay(t, h);
    }
  }

  // Xử lý lệnh điều khiển LED từ UDP (ESP8266)
  handleUDP();

  // Xử lý yêu cầu từ Server AI (Python)
  handleWebRequests();
}

void updateDisplay(float t, float h) {
  tft.fillRect(0, 50, 160, 60, ST77XX_BLACK);
  tft.setTextSize(2);
  tft.setCursor(10, 60);
  tft.setTextColor(ST77XX_CYAN);
  tft.printf("T:%.1f C", t);
  tft.setCursor(10, 90);
  tft.setTextColor(ST77XX_GREEN);
  tft.printf("H:%.1f %%", h);
}

void handleUDP() {
  int packetSize = udp.parsePacket();
  if (packetSize) {
    char buf[50];
    int len = udp.read(buf, sizeof(buf) - 1);
    if (len > 0) {
      buf[len] = '\0';
      String msg = String(buf);
      if (msg == "BTN1_ON") digitalWrite(LED1, HIGH);
      else if (msg == "BTN1_OFF") digitalWrite(LED1, LOW);
      else if (msg == "BTN2_ON") digitalWrite(LED2, HIGH);
      else if (msg == "BTN2_OFF") digitalWrite(LED2, LOW);
      // Bạn có thể thêm các nút 3, 4 tương tự ở đây
    }
  }
}

void handleWebRequests() {
  WiFiClient client = server.available();
  if (client) {
    String req = client.readStringUntil('\r');
    client.flush();

    // Phản hồi JSON cho AI học sâu đọc dữ liệu
    if (req.indexOf("/json") != -1) {
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: application/json");
      client.println("Access-Control-Allow-Origin: *");
      client.println();
      client.printf("{\"temp\": %.2f, \"hum\": %.2f}", currentTemp, currentHum);
    } 
    // Giao diện web cứu cánh khi không có server AI
    else {
      String html = "<html><head><meta charset='utf-8'></head><body>";
      html += "<h1>ESP32 Cảm biến Nấm</h1>";
      html += "<p>IP này dùng để cấu hình vào Python AI: " + WiFi.localIP().toString() + "</p>";
      html += "</body></html>";
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: text/html");
      client.println();
      client.print(html);
    }
    client.stop();
  }
}