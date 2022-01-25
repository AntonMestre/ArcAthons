import Microphone as mic
import asyncio

import time
#self, device, id, callback, channels = [1], window=200, interval=30, blocksize=None, samplerate=None, downsample=10

def test():
    print("test")


# rode 13
# 11
# 14
m1 = mic.Microphone(13,1,test)  
m2 = mic.Microphone(14,2,test)
m3 = mic.Microphone(11,3,test)

m1.test()
m2.test()
m3.test()