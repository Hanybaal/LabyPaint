import pygame
import os
import ctypes
pygame.init()


class Graphismes(pygame.sprite.Sprite):
    def __init__(self, diviseur, niveauActuel):
        super().__init__()
        usr32 = ctypes.windll.user32
        self.tx = usr32.GetSystemMetrics(0)
        self.ty = usr32.GetSystemMetrics(1)

        self.centre = [int(self.tx/2), int(self.ty)/2]
        self.pas = int(self.ty/diviseur)
        self.pasCellule = self.pas
        self.origineX = self.centre[0] - self.pas*(diviseur/2)
        self.origineY = 0
        self.images = {}
        self.niveauActuel = niveauActuel

        self.fen = pygame.display.set_mode((self.tx, self.ty), pygame.FULLSCREEN)

    def getNiveauActuel(self):
        return self.niveauActuel

    def changeNiveauActuel(self, nouveauNiveauActuel):
        self.niveauActuel = nouveauNiveauActuel

    def afficheGrille(self, grille):
        self.pasCellule = int(self.ty/len(grille))
        for ligne in grille:
            for cellule in ligne:
                self.afficheCellule(cellule)


    def deplaceJoueur(self, casesParcourues, direction, grille):
        if len(casesParcourues) == 0:
            return

        j = self.images["textures"]["general"]["player"]
        x = casesParcourues[0].getX()*self.pas + self.getOrigineX()
        y = casesParcourues[0].getY()*self.pas + self.getOrigineY()

        if len(casesParcourues) == 1:
            self.afficheCellule(casesParcourues[0])
            self.fen.blit(j, (x, y))
            
            infos = casesParcourues[0].getInformations(grille)
            self.afficheFrioritures(casesParcourues[0], infos)
            pygame.display.flip()
            return
            
        
        diviseur = 10
        add = (self.pas)/diviseur
        caseActuelle = casesParcourues[0]
        infos = caseActuelle.getInformations(grille)

        for cmp in range(diviseur + 1):
            self.afficheCellule(caseActuelle)
            self.afficheFrioritures(caseActuelle, infos)
            self.fen.blit(j, (x, y))
            x += direction[0]*add
            y += direction[1]*add
            pygame.display.flip()

        self.afficheCellule(caseActuelle)
        self.afficheFrioritures(caseActuelle, infos)
        self.deplaceJoueur(casesParcourues[1:], direction, grille)    
    
    def affichePlayer(self, p):
        x, y = p.getX()*self.pas, p.getY()*self.pas
        self.fen.blit(self.images["textures"]["general"]["player"],
                     (self.getOrigineX() + x, self.getOrigineY() + y))

        
    def afficheCellule(self, cellule):
        niveauActuel = self.getNiveauActuel()[:-1]
        x, y = cellule.getX()*self.pasCellule, cellule.getY()*self.pasCellule
        self.fen.blit(self.images["textures"][niveauActuel][str(cellule.getEtat())],
                     (self.getOrigineX() + x, self.getOrigineY() + y))

    def afficheFrioritures(self, cellule, infos):
        niveauActuel = self.getNiveauActuel()
        x, y = cellule.getX()*self.pasCellule, cellule.getY()*self.pasCellule
        for i in range(len(infos)):
            if infos[i] == "1":
                d = self.convertNumberIntoDirection(i + 1)
                self.fen.blit(self.images["chemin"][niveauActuel[:-1]][d],
                                (self.getOrigineX() + x, self.getOrigineY() + y))
            

    def convertNumberIntoDirection(self, n):
        if n == 1:
            return "haut"

        if n == 2:
            return "droite"

        if n == 3:
            return "bas"

        if n == 4:
            return "gauche"


    def loadTextures(self, niveauActuel : str):
        images = {}
        path = "./img/"
        namedir = [f for f in os.listdir(path)]
        for f in namedir:
            images[f] = {}
            path = "./img/" + f + "/"
            worldnames = [file for file in os.listdir(path)]
            for world in worldnames:
                images[f][world] = {}
                path = "./img/" + f + "/" + world + "/"
                filenames = [file for file in os.listdir(path)]
                for file in filenames:
                    imagename = os.path.splitext(file)[0]
                    images[f][world][imagename] = pygame.image.load(
                                         os.path.join(path, file)).convert_alpha()

        self.images = images


##        path = "./img/textures/" + niveauActuel
##        filenames = [f for f in os.listdir(path)]
##        for name in filenames:
##            #pygame.image.load("./img/textures/1.png")
##            imagename = os.path.splitext(name)[0]
##            images[imagename] = pygame.image.load(
##                                     os.path.join(path, name)).convert_alpha()
##
##        self.images[niveauActuel] = images
##
##
##        if not "general" in self.images.keys():
##            self.images["general"] = {}
##            pathg = "./img/textures/general"
##            filenames = [f for f in os.listdir(pathg)]
##            for name in filenames:
##                #pygame.image.load("./img/textures/1.png")
##                imagename = os.path.splitext(name)[0]
##                self.images["general"][imagename] = pygame.image.load(
##                                         os.path.join(pathg, name)).convert_alpha()        
##

    def scaleTextures(self, dimensions):
        niveauActuel = self.getNiveauActuel()
        for niv in self.images.items():
            for worlds in niv[1].items():
                for images in worlds[1].items():
                    self.images[niv[0]][worlds[0]][images[0]] = pygame.transform.scale(
                                                    images[1], dimensions)


    def getOrigineX(self):
        return self.origineX

    def getOrigineY(self):
        return self.origineY

    def getPas(self):
        return self.pas


class Menu(Graphismes):
    def __init__(self, diviseur, niveauActuel = ""):
        super().__init__(diviseur, niveauActuel)

    def afficheMenu(self):
        self.fen.blit(self.menu["jouer_button"],
                      self.rectsMenu["jouer_button"])
        pygame.display.flip()

    def optionFinNiveau(self):
        self.fen.blit(self.menu["ns"],
                      self.rectsMenu["ns"])
        pygame.display.flip()

    def loadMenu(self):
        path = "./img/menu/textures"
        filenames = [f for f in os.listdir(path)]
        self.menu = {}
        for name in filenames:
            imagename = os.path.splitext(name)[0]
            self.menu[imagename] = pygame.image.load(
                                   os.path.join(path, name)).convert_alpha()

    def scaleMenu(self):
##        self.menu["jouer_button"] = pygame.transform.scale(self.menu["jouer_button"],
##                                                           (self.pas*2, self.pas*2))

        for n in self.menu.items():
            self.menu[n[0]] = pygame.transform.scale(self.menu[n[0]],
                                                     (self.pas*2, self.pas*2))

    def initRects(self):
        self.rectsMenu = {}
        for name in self.menu.keys():
            self.rectsMenu[name] = self.menu[name].get_rect(center = self.centre)


