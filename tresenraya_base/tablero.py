from numpy.lib.shape_base import expand_dims
from casilla import Casilla

import cv2
import numpy as np
import math




class Tablero:

    def __init__(self, anchotablero=600, altotablero=600):
        
        self.colorjug1=(218,86,29)
        self.colorjug2=(29,48,218)
        self.colorganajug1=(218,145,29)
        self.colorganajug2=(77,91,218)
        self.colorempate=(31,182,182)
        self.colorrayas=(50,50,50)
        self.grosorrayas=6
        self.grosorfichas=8

        anchotablero=600
        altotablero=600

        self.casillas=[]
        self.anchotablero=anchotablero
        self.altotablero=altotablero

        anchocasilla=anchotablero/3
        altocasilla=altotablero/3
        self.anchocasilla = anchocasilla
        self.altocasilla = altocasilla


        for i in range(0,9):

            columna =i%3
            fila=math.floor(i/3)

            centro = ( int(((anchocasilla*columna)+(anchocasilla*(columna+1)))/2) , int(((altocasilla*fila)+(altocasilla*(fila+1)))/2))

            nuevacasilla= Casilla(i,anchocasilla,altocasilla, centro)
            self.casillas.append(nuevacasilla)

    def ponerfichaind(self, jug, indice):

        if self.casillas[indice].getValor()==None:
            self.casillas[indice].setValor(jug)
            return True
        else:
            return False
        
    def ponerficharaton(self, jug, x, y):
        
        for i in range(0,9):

            columna =i%3
            fila=math.floor(i/3)

            if (x > int(self.anchocasilla*columna) 
               and x < int(self.anchocasilla*(columna+1))
               and y > int(self.altocasilla*fila)
               and y < int(self.altocasilla*(fila+1))
               ):
                idcasilla=i
                break

        if self.casillas[idcasilla].getValor()==None:
            self.casillas[idcasilla].setValor(jug)
            return True
        else:
            return False

    def estresenraya(self):
        finpartida=False
        juggana=''
        posicion=-1

        

        if self.casillas[0].getValor() == self.casillas[1].getValor() == self.casillas[2].getValor() != None: #horizontal arriba
            finpartida=True
            posicion=1
            juggana=self.casillas[0].getValor()

        elif self.casillas[3].getValor() == self.casillas[4].getValor() == self.casillas[5].getValor() != None: # horizontal medio
            finpartida=True
            posicion=2
            juggana=self.casillas[3].getValor()

        elif self.casillas[6].getValor() == self.casillas[7].getValor() == self.casillas[8].getValor() != None: # horizontal abajo
            finpartida=True
            posicion=3
            juggana=self.casillas[6].getValor()

        elif self.casillas[0].getValor() == self.casillas[3].getValor() == self.casillas[6].getValor() != None: # vertical 1
            finpartida=True
            posicion=4
            juggana=self.casillas[0].getValor()

        elif self.casillas[1].getValor() == self.casillas[4].getValor() == self.casillas[7].getValor() != None: # vertical 2
            finpartida=True
            posicion=5
            juggana=self.casillas[1].getValor()

        elif self.casillas[2].getValor() == self.casillas[5].getValor() == self.casillas[8].getValor() != None: # vertical 3
            finpartida=True
            posicion=6
            juggana=self.casillas[2].getValor()

        elif self.casillas[0].getValor() == self.casillas[4].getValor() == self.casillas[8].getValor() != None: # diagonal 1
            finpartida=True
            posicion=7
            juggana=self.casillas[0].getValor()

        elif self.casillas[2].getValor() == self.casillas[4].getValor() == self.casillas[6].getValor() != None: # diagonal 2
            finpartida=True
            posicion=8
            juggana=self.casillas[2].getValor()

        elif (self.casillas[0].getValor() != None
            and self.casillas[1].getValor() != None
            and self.casillas[2].getValor() != None
            and self.casillas[3].getValor() != None
            and self.casillas[4].getValor() != None
            and self.casillas[5].getValor() != None
            and self.casillas[6].getValor() != None
            and self.casillas[7].getValor() != None
            and self.casillas[8].getValor() != None
            ):
            finpartida=True
            posicion=0
            juggana=None
        return  finpartida, juggana, posicion

    def imprimetablero(self, contjuego, contj1, contj2, contemp, accion=''):
        self.imagen = 255*np.ones((self.altotablero+300,self.anchotablero,3),dtype=np.uint8)
        colorjug1=self.colorjug1
        colorjug2=self.colorjug2
        colorrayas=self.colorrayas
        grosorrayas=self.grosorrayas
        grosorfichas=self.grosorfichas

        anchotablero=self.anchotablero
        altotablero=self.altotablero
        anchocasilla=int(anchotablero/3)
        altocasilla=int(altotablero/3)


        finpartida, juggana, posicion= self.estresenraya()
        if finpartida:
            if juggana==0:
                colorgana=self.colorganajug1
            elif juggana==1:
                colorgana=self.colorganajug2
            else:
                colorgana=self.colorempate
            
    
            if posicion==1:
                cv2.rectangle(self.imagen,(anchocasilla*0,altocasilla*0),(anchocasilla*3,altocasilla*1),colorgana,-1)
            elif posicion==2:
                cv2.rectangle(self.imagen,(anchocasilla*0,altocasilla*1),(anchocasilla*3,altocasilla*2),colorgana,-1)
            elif posicion==3:
                cv2.rectangle(self.imagen,(anchocasilla*0,altocasilla*2),(anchocasilla*3,altocasilla*3),colorgana,-1)
            elif posicion==4:
                cv2.rectangle(self.imagen,(anchocasilla*0,altocasilla*0),(anchocasilla*1,altocasilla*3),colorgana,-1)
            elif posicion==5:
                cv2.rectangle(self.imagen,(anchocasilla*1,altocasilla*0),(anchocasilla*2,altocasilla*3),colorgana,-1)
            elif posicion==6:
                cv2.rectangle(self.imagen,(anchocasilla*2,altocasilla*0),(anchocasilla*3,altocasilla*3),colorgana,-1)
            elif posicion==7:
                cv2.rectangle(self.imagen,(anchocasilla*0,altocasilla*0),(anchocasilla*1,altocasilla*1),colorgana,-1)
                cv2.rectangle(self.imagen,(anchocasilla*1,altocasilla*1),(anchocasilla*2,altocasilla*2),colorgana,-1)
                cv2.rectangle(self.imagen,(anchocasilla*2,altocasilla*2),(anchocasilla*3,altocasilla*3),colorgana,-1)
            elif posicion==8:
                cv2.rectangle(self.imagen,(anchocasilla*2,altocasilla*0),(anchocasilla*3,altocasilla*1),colorgana,-1)
                cv2.rectangle(self.imagen,(anchocasilla*1,altocasilla*1),(anchocasilla*2,altocasilla*2),colorgana,-1)
                cv2.rectangle(self.imagen,(anchocasilla*0,altocasilla*2),(anchocasilla*1,altocasilla*3),colorgana,-1)
            else:
                cv2.rectangle(self.imagen,(anchocasilla*0,altocasilla*0),(anchocasilla*3,altocasilla*3),colorgana,-1)
        #Dibujando lineas
        cv2.line(self.imagen,(0,altocasilla),(anchocasilla*3,altocasilla),colorrayas,grosorrayas) #primera horizontal
        cv2.line(self.imagen,(0,altocasilla*2),(anchocasilla*3,altocasilla*2),colorrayas,grosorrayas)
        cv2.line(self.imagen,(anchocasilla,0),(anchocasilla,altocasilla*3),colorrayas,grosorrayas)
        cv2.line(self.imagen,(anchocasilla*2,0),(anchocasilla*2, altocasilla*3),colorrayas,grosorrayas)

        for i in self.casillas:
            if i.getValor() ==0:
                cv2.line(self.imagen,(i.centro[0]-70,i.centro[1]-70),(i.centro[0]+70,i.centro[1]+70),colorjug1,grosorfichas)
                cv2.line(self.imagen,(i.centro[0]+70,i.centro[1]-70),(i.centro[0]-70,i.centro[1]+70),colorjug1,grosorfichas)
            elif i.getValor() ==1:
                cv2.circle(self.imagen,(i.centro),70,colorjug2,grosorfichas)
        # font 
        font = cv2.FONT_HERSHEY_SIMPLEX 
                
        # fontScale 
        fontScale = 1
        
        # Blue color in BGR 
        color = (10, 10, 10) 
        
        # Line thickness of 2 px 
        thickness = 2
        cv2.putText(self.imagen, 'JUG1', (50, self.altotablero+250) , font, fontScale, colorjug1, thickness, cv2.LINE_AA) 
        cv2.putText(self.imagen, 'EMP', (250, self.altotablero+250) , font, fontScale, color, thickness, cv2.LINE_AA) 
        cv2.putText(self.imagen, 'JUG2', (450, self.altotablero+250) , font, fontScale, colorjug2, thickness, cv2.LINE_AA) 
        cv2.putText(self.imagen, str(contj1), (50, self.altotablero+290) , font, fontScale, colorjug1, thickness, cv2.LINE_AA) 
        cv2.putText(self.imagen, str(contemp), (250, self.altotablero+290) , font, fontScale, color, thickness, cv2.LINE_AA) 
        cv2.putText(self.imagen, str(contj2), (450, self.altotablero+290) , font, fontScale, colorjug2, thickness, cv2.LINE_AA) 
        
        cv2.putText(self.imagen, 'N: '+str(contjuego), (50, self.altotablero+150) , font, fontScale, color, thickness, cv2.LINE_AA) 
        cv2.putText(self.imagen, accion, (350, self.altotablero+150) , font, fontScale, color, thickness, cv2.LINE_AA) 

        
        cv2.imshow('imagen',self.imagen)

    def casillaslibres(self):
        pass

