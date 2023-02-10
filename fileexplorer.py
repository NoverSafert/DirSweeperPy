from os import path
import os


def isValidPath(currentPath):
	if path.exists(currentPath) is False:
		raise Exception("Path not valid")

def isValidFile(filePath):
	directory = path.dirname(filePath)
	print(directory)
	isValidPath(directory)
	if path.isfile(filePath) is False:
		raise Exception("File not found")

def hasChildren(currentPath):
	#hacer una lista con todos los objetos del directorio, iterarsobre estos
	absolute = path.abspath(currentPath)
	dirList = list(os.listdir(path.dirname(absolute)))
	print(dirList)
	
