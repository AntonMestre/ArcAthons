import sys
import threading
import numpy as np
import sounddevice as sd


class Microphone:
    def __init__(self, device, id, callback, maxAmplitude=2, channels=[1], samplerate=None):
        self.channels = channels
        self.device = device
        self.id = id
        self.callback = callback
        self.samplerate = samplerate
        self.maxAmplitude = maxAmplitude

    def start(self):
        threading.Thread(target=self.process).start()

    def audio_callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        # indata est un tableau de table du style
        # [
        #    [float32],
        #    ...
        #    [float32]
        # ]
        # qui correspond à échantillon sur 1s/?

        amplitude = np.linalg.norm(indata)

        if(amplitude >= self.maxAmplitude):
            self.callback(self.id)

    def process(self):
        try:
            if self.samplerate is None:
                device_info = sd.query_devices(self.device, 'input')
                self.samplerate = device_info['default_samplerate']

            with sd.InputStream(
                    device=self.device, channels=max(self.channels),
                    samplerate=self.samplerate, callback=self.audio_callback):
                commande = input()
                stopCommande = 's' + str(self.id)
                if commande == stopCommande:
                    print("Stop " + str(self.id) + " by user")
                    exit()

        except Exception as e:
            print(type(e).__name__ + ': ' + str(e))
