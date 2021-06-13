import cv2
import numpy as np
import math
from tablero import Tablero




class Juego:

    def __init__ (self):
        self.tablero=Tablero(600, 600)
        self.jugador=0
        self.resultadosfinales=False
        self.partidaterminada=False
        


    def evento_raton(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            if(self.resultadosfinales==True):
                self.partidaterminada=True
            else:
                        
                self.tablero.ponerficharaton(self.jugador,x,y)
            
                if self.jugador==0:
                    self.jugador=1
                else:
                    self.jugador=0
            


class qlearning3enraya():

    def __init__ (self, iteraciones):
        self.totalpartidas=iteraciones
        self.contjuego=0
        self.contj1=0
        self.contj2=0
        self.contemp=0


    def jugar(self):
        while (self.contjuego<self.totalpartidas):
            self.contjuego=self.contjuego+1

            juego=Juego()

            juego.tablero.imprimetablero(self.contjuego, self.contj1, self.contj2, self.contemp)
            jugador=juego.jugador


            #Loop mientras no termine la partida
            while (juego.partidaterminada is False):

                cv2.setMouseCallback('imagen', juego.evento_raton)    

                finpartida, juggana, posicion =juego.tablero.estresenraya()

                if jugador != juego.jugador:
                    accion=''

                    #print('cambio de jugador')

                    jugador=juego.jugador

                    if (finpartida):
                        juego.resultadosfinales=True

                        if (juggana is None):
                            print('EMPATE')
                            accion='EMPATE'
                            self.contemp=self.contemp+1

                        else:
                            print(f'Fin de la partida!! Gana el jugador {juggana}. Tablero en posicion {posicion}')
                            accion='JUG-'+str(juggana+1)

                            if juggana==0:
                                self.contj1=self.contj1+1
                            else:
                                self.contj2=self.contj2+1

                    juego.tablero.imprimetablero(self.contjuego, self.contj1, self.contj2, self.contemp, accion)
                    
                k = cv2.waitKey(20) & 0xFF

        cv2.destroyAllWindows()



tresenraya=qlearning3enraya(iteraciones=3)
tresenraya.jugar()


