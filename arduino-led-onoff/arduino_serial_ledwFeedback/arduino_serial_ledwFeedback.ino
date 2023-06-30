const int LED_PIN = 13;
const byte CONTROL_PACKET_SIZE = 4;
const byte FEEDBACK_PACKET_SIZE = 4;
const byte CONTROL_PACKET_HEADER = 0x1A;
const byte FEEDBACK_PACKET_HEADER = 0x2A;
const byte CONTROL_PACKET_COMMAND_INDEX = 1;
const byte CONTROL_PACKET_STATE_INDEX = 2;
const byte FEEDBACK_PACKET_STATE_INDEX = 2;

byte controlPacket[CONTROL_PACKET_SIZE] = {0};
byte feedbackPacket[FEEDBACK_PACKET_SIZE] = {0};

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  if (Serial.available() >= CONTROL_PACKET_SIZE) {
    Serial.readBytes(controlPacket, CONTROL_PACKET_SIZE);

    if (controlPacket[0] == CONTROL_PACKET_HEADER) {
      byte command = controlPacket[CONTROL_PACKET_COMMAND_INDEX];
      byte state = controlPacket[CONTROL_PACKET_STATE_INDEX];

      if (command == 0x10) {
        if (state == 0x01) {
          // Turn on LED
          digitalWrite(LED_PIN, HIGH);
          sendFeedbackPacket(true);
        } else if (state == 0x00) {
          // Turn off LED
          digitalWrite(LED_PIN, LOW);
          sendFeedbackPacket(false);
        }
      }
    }
  }
}

void sendFeedbackPacket(bool state) {
  feedbackPacket[0] = FEEDBACK_PACKET_HEADER;
  feedbackPacket[1] = 0x10;
  feedbackPacket[FEEDBACK_PACKET_STATE_INDEX] = state ? 0x01 : 0x00;
  feedbackPacket[3] = 0xAF;

  Serial.write(feedbackPacket, FEEDBACK_PACKET_SIZE);
}
