from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glutWireTeapot(0.5)

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)

def keyboard(key, x, y):
    print(key)
    # press space key to exit
    if key == b' ':
        sys.exit( )

def idle():
    glutPostRedisplay()

if __name__ == '__main__':
    glutInit()

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutCreateWindow('Hello world!')
    glutReshapeWindow(512, 512)
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutKeyboardFunc(keyboard)

    glutMainLoop()
