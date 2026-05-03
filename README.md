# Voice-using-Volume-Controller

A background Python service that utilizes on-device Edge AI to capture ambient audio and autonomously reduce Windows system volume when a specific trigger phrase (used Hey Jarvis) is detected.

## Core Features
- **Zero-Latency Inference:** Uses ONNX Runtime for near-instantaneous local detection.
- **Hardware Integration:** Directly manipulates system endpoints via the Windows Core Audio API (`pycaw`).
- **Privacy-First:** Audio is processed entirely on-device; no data is sent to the cloud.

## Technical Stack
- **AI Model:** `openWakeWord` running on the ONNX framework.
- **Audio Capture:** Asynchronous thread processing via `sounddevice`.
- **System Control:** `pycaw` for low-level OS volume control.
