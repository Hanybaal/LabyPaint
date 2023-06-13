from GeneratorGrid import *
from tkinter import *
import os
import ctypes

class ManualGenerator(Tk):
    def __init__(self):
        Tk.__init__(self)
        usr32 = ctypes.windll.user32
        self.creerWidgets()
        self.fenInfos = TkInfos(FenSizeInfos(usr32.GetSystemMetrics(0),
                                             usr32.GetSystemMetrics(1),
                                             11, 11), self, self.can)
        self.grille = GeneratorGrid(0, 0)
        self.graphicGrid = [[None for i in range(self.getSizeX())] for j in range(self.getSizeY())]


        #Partie Bind: on associe les touches et la souris à des rôles
        self.bind('<Key>', self.optionsClavier)


    def afficheGrid(self):
        can = self.getCan()
        maxX = self.getSizeX()
        maxY = self.getSizeY()
        ox = maxY/2
        oy = 0
        pasX = (maxX - ox)/len(self.grille.grid[0])
        pasY = maxY/len(self.grille.grid)
        i, j = -1, -1
        for ligne in self.grille.grid:
            i += 1
            j = -1
            for cell in ligne:
                j += 1
                origineX = ox + pasX*cell.getX()
                origineY = oy + pasY*cell.getY()
                cell.graphicCell = can.create_rectangle(
                                         origineX, origineY, origineX + pasX, origineY + pasY,
                                         fill = self.grille.stateToColor(cell.getState()), outline = "red")
                cell.initBinds(can)
        can.update()


    def affStateCell(self, cellule):
        y, x = cellule.getY(), cellule.getX()
        g = self.grille.grid
        self.can.itemconfigure(self.graphicGrid[y][x], fill = self.grille.stateToColor(cellule.getState))

    def optionsClavier(self, event):
        touche = event.keysym
        if touche == "Escape":
            self.quitter()

        if touche == "Return":
            res = self.tabSize.get()
            if (res != ""):
                if ('+' in res):
                    estUnChiffre = lambda car : (car in "1234567890" and (len(car) == 1))
                    n, m = 0, 0
                    car = res[0]
                    while(estUnChiffre(car)):
                        n += 1
                        car = res[n]
                        
                    newY = int(res[:(n)])
                    newX = int(res[(n+1):])
                    print(newX, newY)
                    self.grille = GeneratorGrid(newY, newX)
##                    self.fenInfos.changePasX(newX)
##                    self.fenInfos.changePasY(newY)
                    self.afficheGrid()
                    self.update()

                

    def quitter(self):
        self.destroy()

    def genFile(self):
        name = input("Rentrez un nom de fichier: ")
        file = open(name + ".txt", "w")
        g = self.grille
        for ligne in g.grid:
            for cel in ligne:
                s = cel.getState()
                file.write(str(s))
            file.write('\n')
        file.close()
            


    ##Fonctions get
    def getFen(self):
        return self.fenInfos.getFen()

    def getCan(self):
        return self.fenInfos.getCan()

    def getSizeX(self):
        return self.fenInfos.getSizeX()

    def getSizeY(self):
        return self.fenInfos.getSizeY()

    def getPasX(self):
        return self.fenInfos.getPasX()

    def getPasY(self):
        return self.fenInfos.getPasY()
    
    ##Fonctions génératrices
    def creerWidgets(self):
        usr32 = ctypes.windll.user32
        self.can = Canvas(self, bg = "grey", height = usr32.GetSystemMetrics(1),
                              width = usr32.GetSystemMetrics(0))
        self.can.pack(side = LEFT)
    

        self.tabSize = Entry(self, width = 25)
        self.tabSize.place(x = 0, y = 20)

        self.validButton = Button(self, text = "Valider le niveau", command = self.genFile)
        self.validButton.place(x = 200, y = 0)

        info = Label(self, text = "Taille du tableau sous forme y+x")
        info.place(x = 0, y = 0)



class FenSizeInfos():
    def __init__(self, sx, sy, cx, cy):
        self.sx = sx
        self.sy = sy
        self.changePasX(cx)
        self.changePasY(cy)

    ##Fonctions génératrices
    def changeSizeX(self, v):
        self.sx = v

    def changeSizeY(self, v):
        self.sy = v

    def changePasX(self, c):
        if (c == 0):
            c = 1
        self.px = self.getSizeX()/c

    def changePasY(self, c):
        if (c == 0):
            c = 1
        self.py = self.getSizeY()/c

    ##Fonctions get
    def getSizeX(self):
        return self.sx

    def getSizeY(self):
        return self.sy

    def getPasX(self):
        return self.px

    def getPasY(self):
        return self.py

class TkInfos():
    def __init__(self, sizeInfos, fen, can):
        self.sizeInfos = sizeInfos
        self.fen = fen
        self.can = can


    ##Fonctions génératrices
    def changeSizeX(self, v):
        self.sizeInfos.changeSizeX(v)

    def changeSizeY(self, v):
        self.sizeInfos.changeSizeY(v)

    def changePasX(self, c):
        self.sizeInfos.changePasX(c)

    def changePasY(self, c):
        self.sizeInfos.changePasY(c)

    ##Fonctions get
    def getFen(self):
        return self.fen

    def getCan(self):
        return self.can

    def getSizeX(self):
        return self.sizeInfos.sx

    def getSizeY(self):
        return self.sizeInfos.sy

    def getPasX(self):
        return self.sizeInfos.px

    def getPasY(self):
        return self.sizeInfos.py
        

if __name__ == "__main__":
    app = ManualGenerator()
    usr32 = ctypes.windll.user32
    #app.geometry("" + str(usr32.GetSystemMetrics(0)) + "x" + str(usr32.GetSystemMetrics(1)) + "+1+0")
    app.attributes('-fullscreen', True)
    app.maxsize(app.getSizeX(), app.getSizeY())
    app.minsize(app.getSizeX(), app.getSizeY())
    app.mainloop()
