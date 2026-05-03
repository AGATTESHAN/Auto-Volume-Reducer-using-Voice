from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class VolumeController:
    def __init__(self):
        """Initializes the connection to the Windows master volume."""
        # Grab the default playback device
        self.device = AudioUtilities.GetSpeakers()
        
        # Access the EndpointVolume property directly instead of calling Activate()
        self.volume = self.device.EndpointVolume

    def get_current_volume(self):
        """Returns the current volume as a float between 0.0 and 1.0."""
        return self.volume.GetMasterVolumeLevelScalar()

    def set_volume(self, level):
        """Sets the master volume. Level must be between 0.0 and 1.0."""
        safe_level = max(0.0, min(1.0, level))
        self.volume.SetMasterVolumeLevelScalar(safe_level, None)

    def hush(self, reduction_percentage=0.25):
        """Reduces the current volume by the specified percentage."""
        current_vol = self.get_current_volume()
        print(f"Current Volume: {current_vol * 100:.1f}%")
        
        new_vol = current_vol - reduction_percentage
        self.set_volume(new_vol)
        print(f"Volume reduced to: {max(0.0, new_vol) * 100:.1f}%")

# --- Quick Test Block ---
if __name__ == "__main__":
    audio = VolumeController()
    print("Testing Volume Slider...")
    audio.hush(0.25)