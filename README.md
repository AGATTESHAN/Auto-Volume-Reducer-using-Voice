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

## Development Process & Tools
To rapidly prototype and deploy this system, I acted as the system architect and utilized LLMs (like Gemini/ChatGPT) as pair-programming tools.

While AI generated the boilerplate OS-level hooks (pycaw) and assisted with dependency debugging, my core engineering focus was on the system architecture, local model integration, and iterative testing to ensure the pipeline operated in real-time with zero latency. This project heavily exercised my skills in prompt engineering, technical troubleshooting, and system integration.
