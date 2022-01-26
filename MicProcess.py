import time
import Traitement as traitement
import TurtleManager as turtle
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
        value = (time.time() - self.startTime) 
        self.tab.append((id,value ))

    def send(self):
        # Marge d'erreur
        # for i in range(len(self.tab)):
        #     if self.tab[i][1] != 0:
        #         self.tab[i] = (self.tab[i][0], self.tab[i][1] - 0.03)
        #     # self.tab[i][1] -= 0.03
        dim = (0.48,0.48)
        coord_m1 = (0,-0.24)
        coord_m2 = (0.24,0.24)
        coord_m3 = (-0.24,0.24)
        print(self.tab)
        position = traitement.traitement(dim,coord_m1,coord_m2,coord_m3,self.tab)
        print("Position : "+ str(position))
        turtleIns = turtle.TurtleManager(dim)
        return turtleIns.draw(position[0],position[1])

    def resetData(self):
        print("RESET DATA")
        self.startTime = None
        self.tab = []

    def add(self, id):
        # print("APRES : "+ str(time.time()))
		# On check si les données actuelles ne sont pas trop vielle
        # if self.startTime != None:
        #     print(time.time() - self.startTime)
        if self.startTime != None and len(self.tab) != 0 and (time.time() - self.startTime) >= self.outdatedTime:
            print("OLD DATA DETECTED RESET NEEDED !")
            self.resetData()

        if self.isDefined(id):
            return


        if len(self.tab) == 0:
            self.initTab(id)
        else:
            self.addNewOne(id)

        if len(self.tab) == self.nbMic:
            self.send()
            self.resetData()
		
        # print(self.tab)
