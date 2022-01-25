import Microphone as mic
import MicProcess as micProcess


def test(id):
    print("[" + str(id) + "] action detected")

micProcess = micProcess.MicProcess(3)

# rode 13
# 11
# 14
m1 = mic.Microphone(2,1,micProcess.add)  
m2 = mic.Microphone(3,2,micProcess.add)
m3 = mic.Microphone(4,3,micProcess.add)

m1.start()
m2.start()
m3.start()