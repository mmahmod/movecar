from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(.01, .85, .9, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)



def build(x,m):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(1,0.2,m)
    glTranslate(-7+x,3.75,-20)
    glutSolidCube(5)
    glColor3f(.91,0.7,.35)
    glTranslate(0,0,2.5)
    glBegin(GL_POLYGON)
    glVertex3d(-2,-2.5,0)
    glVertex3d(-2, -.5, 0)
    glVertex3d(-.5, -.5, 0)
    glVertex3d(-.5, -2.5, 0)
    glEnd()
    glColor3f(.1,.065,.9)
    glBegin(GL_POLYGON)
    glVertex3d(-2, 2, 0)
    glVertex3d(-2, 1, 0)
    glVertex3d(-.5, 1, 0)
    glVertex3d(-.5, 2, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3d(2, 2, 0)
    glVertex3d(2, 1, 0)
    glVertex3d(.5, 1, 0)
    glVertex3d(.5, 2, 0)
    glEnd()
    glPopAttrib()
    glPopMatrix()





def bordery(x,z):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(0,0,1)
    glTranslate(x,-1.25,z)
    glScale(3,1,1)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

def bordero(x,z):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(1,1,1)
    glTranslate(x,-1.25,z)
    glScale(3,1,1)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

def whitesign(x1,x2):
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    glVertex3d(x1,-1.25,1)
    glVertex3d(x1, -1.25, -1)
    glVertex3d(x2, -1.25, -1)
    glVertex3d(x2, -1.25, 1)
    glEnd()

def road():
    glBegin(GL_POLYGON)
    glColor3f(0,0,0)
    glVertex3d(-50,-1.25,5)
    glVertex3d(-50,-1.25,-5)
    glVertex3d(20,-1.25,-5)
    glVertex3d(20,-1.25,5)
    glEnd()
    whitesign(-50, -30)
    whitesign(-25, -15)
    whitesign(-10, -5)
    whitesign(0, 5)
    whitesign(10, 20)
    for i in range(-50,20,6):
        bordery(i,5)
        bordero(i+3,5)
    for i in range(-50,20,6):
        bordery(i,-5)
        bordero(i+3,-5)
x=0
angle=0
deltax=0.001
deltaangle=-0.1
def draw1():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global angle
    global deltax
    global deltaangle
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    road()
    
    glColor3f(1,0,0)
    glScale(1,0.25,0.5)
    glTranslate(x,0,0)
    glutWireCube(5)

    glLoadIdentity()
    glTranslate(x,0.25*5,0)
    glScale(0.5,0.25,0.5)
    glutWireCube(5)

    glColor3f(0,0,1)
    glLoadIdentity()
    glTranslate(x+2.5,-2.5*0.25,2.5*0.5)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)


    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x+2.5, -2.5 * 0.25, -2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * 0.25, 2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * 0.25, -2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)

    glColor3f(0, 1, 0)
    glLoadIdentity()
    glTranslate(x+2.3, 2*0.25, 1.5*0.5)
    glutWireSphere(.25,50,50)

    glColor3f(0, 1, 0)
    glLoadIdentity()
    glTranslate(x+2.3, 2 * 0.25, -1.5 * 0.5)
    glutWireSphere(.25, 50, 50)
    x=x+deltax
    angle=angle+deltaangle
    if x>=10:
        deltax=-0.1
        deltaangle= 0.1
    ##########################################################-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif x<=-10:
        deltax= 0.1
        deltaangle= 0.1

    glFlush()





glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,550)
glutCreateWindow(b"Moving car")
glutDisplayFunc(draw1)
glutIdleFunc(draw1)
myinit()
glutMainLoop()
