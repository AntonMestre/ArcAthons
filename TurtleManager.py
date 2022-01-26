from turtle import *

class TurtleManager:
    def __init__(self,dim):
        self.dcl = 10
        self.w = 1000
        self.h = 1000
        self.coef = self.w / dim[0] 
        print("COEF : " + str(self.coef))
        
    def init(self):
        speed(0)
    
        screensize(self.w,self.h)
        penup()
        goto(-self.w/2,0)
        pendown()
        fd(self.w)
        penup()
        goto(0,self.w/2)
        pendown()
        rt(90)
        fd(self.w)
        rt(-90)
        penup()

    def draw(self,x,y):

        x *= self.coef
        y *= self.coef

        print("X = " + str(x))
        print("Y = " + str(y))
        self.init()
        penup()
        goto(x-self.dcl,y)
        pendown()
        fd(self.dcl*2)
        penup()
        goto(x,y+self.dcl)
        pendown()
        rt(90)
        fd(self.dcl*2)
        rt(-90)
        penup()
        done()
