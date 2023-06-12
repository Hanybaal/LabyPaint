from tkinter import *

class GeneratorGrid():
    def __init__(self, y, x):
        self.maxX = x
        self.maxY = y
        self.grid = [[GeneratorCell(y, x) for x in range(self.maxX)] for y in range(self.maxY)]

    def getMaxX(self):
        return self.maxX

    def getMaxY(self):
        return self.maxY

    def stateToColor(self, s):
        if (s == 0):
            return "black"

        if (s == 1):
            return "green"


class GeneratorCell():
    def __init__(self, y, x, etat = 0):
        self.x = x
        self.y = y
        self.etat = etat
        self.graphicCell = None

    def __repr__(self):
        return (str(self.getY()) + ":" + str(self.getX()))


    def initBinds(self, can):
        self.can = can
        gc = self.graphicCell
        can.tag_bind(gc, "<ButtonRelease>", self.changeStateGraphic)
        can.tag_bind(gc, "<Enter>", self.hoverCel)
        can.tag_bind(gc, "<Leave>", self.unhoverCel)

    def afficheCellule(self, event):
        self.can.itemconfigure(self.graphicCell, fill = self.stateToColor())

    def hoverCel(self, event):
        self.can.itemconfigure(self.graphicCell, outline = "aquamarine")

    def unhoverCel(self, event):
        self.can.itemconfigure(self.graphicCell, outline = "red")

    def stateToColor(self):
        listeColor = ["black", "green"]
        return listeColor[self.getState()]

    #Fonctions génératrices
    def changeStateGraphic(self, event):
        self.changeState()
        self.afficheCellule(event)

    def changeState(self):
        self.etat += 1
        self.etat %= 2
    
    #Fonctions get
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getState(self):
        return self.etat
