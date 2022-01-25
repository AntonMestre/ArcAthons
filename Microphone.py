import queue
import sys
import threading

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

class Microphone:
    def __init__(self, device, id, callback, channels = [1], window=200, interval=30, blocksize=None, samplerate=None, downsample=10):
        self.channels = channels
        self.device = device
        self.id = id
        self.callback = callback
        self.window = window
        self.interval = interval 
        self.blocksize = blocksize
        self.samplerate = samplerate
        self.downsample = downsample
        self.q = queue.Queue()
        self.mapping = [c - 1 for c in self.channels]
        self.lines = None
        self.plotdata = None

    def test(self):
        threading.Thread(target=self.start).start()

    def audio_callback(self,indata, frames, time, status):
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

        print(amplitude)

        #FILTRE CUSTOM LOL
        if(amplitude < 3):
            for i in range(len(indata)):
                indata[i] = [0.0]
        else:
            self.callback()
        
        self.q.put(indata[::self.downsample, self.mapping])


    def update_plot(self,frame):
        """This is called by matplotlib for each plot update.
        Typically, audio callbacks happen more frequently than plot updates,
        therefore the queue tends to contain multiple blocks of audio data.
        """
        while True:
            try:
                data = self.q.get_nowait()
            except queue.Empty:
                break


            #print(data[0][0])
            #if(data[0][0] < np.float32("8.0")):
            #    data[0][0] = np.float32("0.0")

            shift = len(data)
            # print("========")
            # print(data)
            # print(data[0][0])
            # print(shift)
            


            self.plotdata = np.roll(self.plotdata, -shift, axis=0)
            self.plotdata[-shift:, :] = data
        for column, line in enumerate(self.lines):
            line.set_ydata(self.plotdata[:, column])
        return self.lines


    def start(self):
        try:
            # Namespace(list_devices=False, channels=[1], device=None, window=200, interval=30, blocksize=None, samplerate=None, downsample=10)
            if self.samplerate is None:
                device_info = sd.query_devices(self.device, 'input')
                self.samplerate = device_info['default_samplerate']

            
            # length = int(self.window * self.samplerate / (1000 * self.downsample))
            # self.plotdata = np.zeros((length, len(self.channels)))

            # fig, ax = plt.subplots()
            # self.lines = ax.plot(self.plotdata)
            # if len(self.channels) > 1:
            #     ax.legend(['channel {}'.format(c) for c in self.channels],
            #             loc='lower left', ncol=len(self.channels))

            # ax.axis((0, len(self.plotdata), -1, 1))
            # ax.set_yticks([0])
            # ax.yaxis.grid(True)
            # ax.tick_params(bottom=False, top=False, labelbottom=False,
            #             right=False, left=False, labelleft=False)
            # fig.tight_layout(pad=0)
            print("DEBUT STREAM")
            stream = sd.InputStream(
                device=self.device, channels=max(self.channels),
                samplerate=self.samplerate, callback=self.audio_callback)
            # ani = FuncAnimation(fig, self.update_plot, interval=self.interval, blit=True)
        
            # with stream:
            #     plt.show()
        except Exception as e:
            print(type(e).__name__ + ': ' + str(e))
    