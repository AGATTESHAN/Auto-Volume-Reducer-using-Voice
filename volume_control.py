from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class VolumeController:
    def __init__(self):
        self.device = AudioUtilities.GetSpeakers()
        self.volume = self.device.EndpointVolume

    def get_current_volume(self):
        return self.volume.GetMasterVolumeLevelScalar()

    def set_volume(self, level):
        safe_level = max(0.0, min(1.0, level))
        self.volume.SetMasterVolumeLevelScalar(safe_level, None)

    def hush(self, reduction_percentage=0.25):
        current_vol = self.get_current_volume()
        print(f"Current Volume: {current_vol * 100:.1f}%")
        
        new_vol = current_vol - reduction_percentage
        self.set_volume(new_vol)
        print(f"Volume reduced to: {max(0.0, new_vol) * 100:.1f}%")

if __name__ == "__main__":
    audio = VolumeController()
    print("Testing Volume Slider...")
    audio.hush(0.25)
