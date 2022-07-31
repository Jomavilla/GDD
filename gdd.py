import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

#Definindo os vértices do objeto e configurações
def draw1():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3d(0.0, 1.0, 0.0)
    glBegin(GL_LINE_LOOP)
    #Quadrado maior do capacete
    glVertex2d(3,12)
    glVertex2d(9,12)
    glVertex2d(9,8)
    glVertex2d(3,8)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #quadrado menor esquerda
    glVertex2d(4,11)
    glVertex2d(5,11)
    glVertex2d(5,10)
    glVertex2d(4,10)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #quadrado maior direita
    glVertex2d(7,11)
    glVertex2d(8,11)
    glVertex2d(8,10)
    glVertex2d(7,10)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #Parte Esquerda
    glVertex2d(2,11)
    glVertex2d(3,11)
    glVertex2d(3,8)
    glVertex2d(2,8)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #Parte Esquerda 2
    glVertex2d(1,9)
    glVertex2d(2,9)
    glVertex2d(2,4)
    glVertex2d(1,4)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #Parte Esquerda 3
    glVertex2d(1,5)
    glVertex2d(3,5)
    glVertex2d(3,4)
    glVertex2d(1,4)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #Parte Esquerda 4
    glVertex2d(2,5)
    glVertex2d(3,5)
    glVertex2d(3,1)
    glVertex2d(2,1)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #Parte Baixa
    glVertex2d(2,2)
    glVertex2d(6,2)
    glVertex2d(6,1)
    glVertex2d(2,1)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #Parte Baixa 2
    glVertex2d(5,1)
    glVertex2d(10,1)
    glVertex2d(10,0)
    glVertex2d(5,0)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #Parte Direita
    glVertex2d(9,2)
    glVertex2d(11,2)
    glVertex2d(11,1)
    glVertex2d(9,1)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #Parte Direita 2
    glVertex2d(10,3)
    glVertex2d(12,3)
    glVertex2d(12,2)
    glVertex2d(10,2)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #Parte Direita 3
    glVertex2d(10,9)
    glVertex2d(12,9)
    glVertex2d(12,3)
    glVertex2d(10,3)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #Parte Direita 4
    glVertex2d(10,10)
    glVertex2d(11,10)
    glVertex2d(11,9)
    glVertex2d(10,9)
    glEnd()
    glFlush()
    glBegin(GL_LINE_LOOP)
    #Parte Direita 5
    glVertex2d(9,11)
    glVertex2d(10,11)
    glVertex2d(10,7)
    glVertex2d(9,7)
    glEnd()
    glFlush()

#Iniciando a main eo pygame para modelar o objeto
def main():
    pygame.init()
    display=(500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(150, display[0]/display[1], 1, 10)
    glTranslatef(0.0, 0.0, -5)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #Definir as Transformações Geométricas    
            draw1() 
            if event.type == pygame.KEYDOWN:
                #Pressionar setinha para ESQUERDA para Escala(diminuir)
                if event.key == pygame.K_LEFT:    
                    glScalef(0.5,0.5,1)
                #Pressionar setinha para DIRETA para Translação    
                if event.key == pygame.K_RIGHT: 
                    glTranslatef(2,2,1)
                #Pressionar setinha para CIMA para Rotação    
                if event.key == pygame.K_UP:     
                    glRotatef(10,2,2,1)
                #Pressionar setinha para BAIXO para Reflexão    
                if event.key == pygame.K_DOWN:     
                    glScalef(-1,1,1)    
        
            pygame.display.flip()
   

if __name__ == "__main__":
    main()