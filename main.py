import Microphone as mic



def test(id):
    print("[" + str(id) + "] action detected")


# rode 13
# 11
# 14
m1 = mic.Microphone(2,1,test)  
m2 = mic.Microphone(3,2,test)
m3 = mic.Microphone(4,3,test)

m1.start()
m2.start()
m3.start()