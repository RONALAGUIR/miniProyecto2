# miniProyecto2
Proeycto enfocado en el desarrollo de agentes inteligentes.# 🖐️ Contador de Dedos con Python, OpenCV, MediaPipe y Arduino

## 🎯 Descripción

Este proyecto desarrolla un sistema de visión por computadora que:

- Detecta entre 0 y 5 dedos levantados usando la cámara web.
- Envía el número detectado al Arduino vía comunicación serial (USB).
- El Arduino suma los números recibidos y muestra el resultado con 4 LEDs simulando un contador binario.

---

## 🧩 Requisitos

### Software
- Python 3.x
- Arduino IDE
- Librerías de Python:
  - OpenCV → `pip install opencv-python`
  - MediaPipe → `pip install mediapipe`
  - PySerial → `pip install pyserial`

### Hardware
- Arduino UNO o Nano
- 4 LEDs
- 4 resistencias de 220Ω
- Protoboard y cables jumper
- Computadora con cámara web

---

## ⚙️ Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala las librerías necesarias:

```bash
pip install opencv-python mediapipe pyserial
