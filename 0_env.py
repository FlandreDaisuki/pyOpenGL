import os
import sys
import OpenGL

if __name__ == '__main__':
	osu = os.uname()
	sysname = osu.sysname
	machine = osu.machine
	release = osu.release
	print('os.uname:\n{} {}\n{}\n'.format(sysname, machine, release))
	print('python version:\n{}\n'.format(sys.version))
	print('pyOpenGL version:', OpenGL.version.__version__)
