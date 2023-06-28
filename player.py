

class Player():
    def __init__(self):
        self.caseActuelle = None

    def selfMove(self, grille, direction : tuple, listeCasesParcourues = []):
        if (self.isVoidDirection(direction)):
            return []
        
        coordx = self.getX() + direction[0]
        coordy = self.getY() + direction[1]
        if grille.isBloqued((coordx, coordy)):
            return listeCasesParcourues

        caseCible = grille.getCellule((coordx, coordy))
        
        self.changeCA(caseCible)
        self.changeX(self.getX() + direction[0])
        self.changeY(self.getY() + direction[1])
        caseCible.passage()

        listeCasesParcourues.append(caseCible)
        
        return self.selfMove(grille, direction, listeCasesParcourues)

    def isVoidDirection(self, direction):
        return (direction == (0, 0))

    def getCA(self):
        return self.caseActuelle

    def changeCA(self, case):
        self.caseActuelle = case

    def getX(self):
        return self.getCA().getX()

    def getY(self):
        return self.getCA().getY()

    def changeX(self, newX):
        self.x = newX

    def changeY(self, newY):
        self.y = newY
