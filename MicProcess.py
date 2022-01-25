import time

class MicProcess:
    def __init__(self, nbMic,outdatedTime = 5):
        self.tab = []
        self.nbMic = nbMic
        self.startTime = None
        self.outdatedTime = outdatedTime

    def isDefined(self,id):
        isDefined = False
        i = 0
        while isDefined == False and i<len(self.tab):
            if self.tab[i][0] == id:
                isDefined = True
            i = i + 1
        return isDefined

    def initTab(self,id):
        self.startTime = time.time()
        self.tab.append((id, 0))

    def addNewOne(self,id):
        self.tab.append((id, (time.time() - self.startTime)))

    def resetData(self):
        print("SEND TO POSITION")
        #code ...
        print("RESET DATA")
        self.startTime = None
        self.tab = []

    def add(self, id):
        if self.isDefined(id):
            return
        

		# On check si les données actuelles ne sont pas trop vielle
        # if self.startTime != None:
        #     print(time.time() - self.startTime)
        
        if self.startTime != None and (time.time() - self.startTime) >= self.outdatedTime:
            print("OLD DATA DETECTED RESET NEEDED !")
            self.resetData()

        l = len(self.tab)

        if l == 0:
            self.initTab(id)
        else:
            self.addNewOne(id)

        if len(self.tab) == self.nbMic:
            self.resetData()
		
        print(self.tab)
