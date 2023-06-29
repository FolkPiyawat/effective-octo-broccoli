#define key_r1 D0
#define key_r2 D1
#define key_r3 D2
#define key_r4 D3
#define lux_r1 D4
#define lux_r2 D5
#define lux_r3 D6
#define lux_r4 D7

int data1;

void setup() {
  Serial.begin(115200);
  pinMode(key_r1, OUTPUT);
  pinMode(key_r2, OUTPUT);
  pinMode(key_r3, OUTPUT);
  pinMode(key_r4, OUTPUT);
  pinMode(lux_r1, OUTPUT);
  pinMode(lux_r2, OUTPUT);
  pinMode(lux_r3, OUTPUT);
  pinMode(lux_r4, OUTPUT);
}

void loop() {

  while (Serial.available())
  {
    data1 = Serial.read();
  }

  Serial.println(data1);

  if (data1 == 97)
    digitalWrite(key_r1, HIGH);
  else if (data1 == 98)
    digitalWrite(key_r1, LOW);
  else if (data1 == 99)
    digitalWrite(key_r2, HIGH);
  else if (data1 == 100)
    digitalWrite(key_r2, LOW);
  else if (data1 == 101)
    digitalWrite(key_r3, HIGH);
  else if (data1 == 102)
    digitalWrite(key_r3, LOW);
  else if (data1 == 103)
    digitalWrite(key_r4, HIGH);
  else if (data1 == 104)
    digitalWrite(key_r4, LOW);
  else if (data1 == 105)
    digitalWrite(lux_r1, HIGH);
  else if (data1 == 106)
    digitalWrite(lux_r1, LOW);
  else if (data1 == 107)
    digitalWrite(lux_r2, HIGH);
  else if (data1 == 108)
    digitalWrite(lux_r2, LOW);
  else if (data1 == 109)
    digitalWrite(lux_r3, HIGH);
  else if (data1 == 110)
    digitalWrite(lux_r3, LOW);
  else if (data1 == 111)
    digitalWrite(lux_r4, HIGH);
  else if (data1 == 112)
    digitalWrite(lux_r4, LOW);
}
