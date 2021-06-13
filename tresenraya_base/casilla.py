class Casilla:

    def __init__(self, numero, anchocasilla, altocasilla, centro):
        self.numcasilla=numero
        self.valor=None
        self.anchocasilla = anchocasilla
        self.altocasilla = altocasilla
        self.centro=centro
    
    def setValor(self, jugador):
        self.valor=jugador

    def getValor(self):
        return self.valor

