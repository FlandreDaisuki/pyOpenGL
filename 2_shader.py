import sys
import numpy as np

from OpenGL.GL import *
from OpenGL.GLUT import *

from OpenGL.arrays import vbo

vertex_code = """
void main() {
    gl_Position = ftransform();
    gl_FrontColor = abs(gl_Position);
}"""

fragment_code = """
void main() {
    gl_FragColor = gl_Color;
}"""


myvbo = vbo.VBO(np.array( [
            [ 0, 1, 0],
            [-1,-1, 0],
            [ 1,-1, 1],
        ],'f'))

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glUseProgram(program)

    try:
        myvbo.bind()
        try:
            glEnableClientState(GL_VERTEX_ARRAY);
            # glVertexPointer( size , type , stride , pointer )
            glVertexPointer(3, GL_FLOAT, 12, myvbo )
            # glDrawArrays( mode , first, count )
            glDrawArrays(GL_TRIANGLES, 0, 9)
        finally:
            myvbo.unbind()
            glDisableClientState(GL_VERTEX_ARRAY);
    finally:
        glUseProgram( 0 )

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

    global program

    # Request a program and shader slots from GPU
    program  = glCreateProgram()
    vertex   = glCreateShader(GL_VERTEX_SHADER)
    fragment = glCreateShader(GL_FRAGMENT_SHADER)
    
    # Set shaders source
    glShaderSource(vertex, vertex_code)
    glShaderSource(fragment, fragment_code)
    
    # Compile shaders
    glCompileShader(vertex)
    glCompileShader(fragment)
    
    # Attach shader objects to the program
    glAttachShader(program, vertex)
    glAttachShader(program, fragment)
    
    # Build program
    glLinkProgram(program)
    
    # Get rid of shaders (no more needed)
    glDetachShader(program, vertex)
    glDetachShader(program, fragment)

    glutMainLoop()
