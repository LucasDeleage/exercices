

```python``

from turtle import *



class House:

    def __init__(self, larg, houseColor, nbrHouse = 1):
        """[summary]

        Args:
            size ([int]): [taille du carré de la maison]
            houseColor ([string]): [couleur de la maison]
            nbrHouse ([int]): [nombre de maison souhaités]
        """
        self.larg = larg
        self.houseColor = houseColor
        self.nbrHouse = nbrHouse
        self.posX, self.posY = -500, 0
        self.start = self._createCity()
        
    def _createCity(self):

        """[summary]

        Créer un nombre de maison égale au nombre placé en paramètre
        de la class
        """

        for i in range(self.nbrHouse):
            
            self._createHouse()
            self.posX += 250
            

        hideturtle()
        exitonclick()

    def _createHouse(self):

        """[summary]
        Créer le modèle d'une maison
        """

        penup()
        goto(self.posX, self.posY)
        pendown()
        pensize(3)
        color(self.houseColor) 
        begin_fill()
        for i in range(4):
            forward(self.larg)
            left(90)
        end_fill()


        
        penup()
        goto(self.posX - 20, self.larg)
        pendown()
        begin_fill()
        for i in range(3): 
            forward(self.larg + 40)
            left(120)
        end_fill()

        

        
ny = House(150, "yellow")
