import Microphone as mic
import MicProcess as micProcess



micProcess = micProcess.MicProcess(3)

# # rode 13
# # 11
# # 14
m1 = mic.Microphone(13,1,micProcess.add,1)  #rode
m2 = mic.Microphone(11,2,micProcess.add,2) 
m3 = mic.Microphone(14,3,micProcess.add,2)

m1.start()
m2.start()
m3.start()