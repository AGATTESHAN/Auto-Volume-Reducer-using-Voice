
import sounddevice as sd
import numpy as np
from openwakeword.model import Model
from volume_control import VolumeController 

audio_controller = VolumeController()
oww_model = Model(wakeword_models=["hey_jarvis_v0.1.onnx"], inference_framework="onnx")

def audio_callback(indata, frames, time, status):
    audio_data = indata.flatten()
    oww_model.predict(audio_data)
    for mdl in oww_model.prediction_buffer.keys():
        if oww_model.prediction_buffer[mdl][-1] > 0.5:
            print("\n🎯 WAKE WORD DETECTED!")
            print("Action: Triggering Volume Reducer...")
            audio_controller.hush(0.25)
            oww_model.reset()

print("Auto-Hush System Active. Say 'Hey Jarvis' to reduce volume.")
with sd.InputStream(samplerate=16000, channels=1, blocksize=1280, dtype='int16', callback=audio_callback):
    while True:
        sd.sleep(1000)

        