// Pines donde están conectados los LEDs
int leds[] = {2, 3, 4, 5}; // 4 LEDs: bit 0, bit 1, bit 2, bit 3

int acumulador = 0;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 4; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    int dedos = data.toInt();
    acumulador += dedos;

    if (acumulador > 15) acumulador = 0; // Resetea si pasa de 15 (4 bits máximo)

    mostrarNumero(acumulador);
  }
}

void mostrarNumero(int numero) {
  for (int i = 0; i < 4; i++) {
    digitalWrite(leds[i], (numero >> i) & 1);
  }
}
