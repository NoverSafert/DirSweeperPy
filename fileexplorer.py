from os import path
import os


def isValidPath(currentPath):
	if path.exists(currentPath) is False:
		raise NotADirectoryError("Directory not found")

def isValidFile(filePath):
	directory = path.dirname(filePath)
	print(directory)
	isValidPath(directory)
	if path.isfile(filePath) is False:
		raise FileNotFoundError("FileNotFound")

def getAbsolutePath(currentPath):
	return path.abspath(currentPath)

def getDirContents(currentPath):
	return list(os.listdir(getAbsolutePath(currentPath)))
	
##TODO: corregir rutas hijo, idea solución (agregar el currentpath a la dirección dada o convertir todo a un absolute path)
def getChildrenFolder(currentPath):
	dirContent = getDirContents(currentPath)
	removeIndexes = []
	##quita directorios images y txt
	for index in range(len(dirContent)):
		fullPath = currentPath + "\\" + dirContent[index]
		if not path.isdir(fullPath):
			removeIndexes.append(dirContent[index])
		else:
			dirContent[index] = fullPath

	for toRemove in removeIndexes:
		dirContent.remove(toRemove)

	if len(dirContent) == 0:
		return False
	else:
		
		return dirContent
	

def getChildrenFiles(currentPath):
	dirContent = getDirContents(currentPath)
	removeIndexes = []
	for index in range(len(dirContent)):
		fullPath = currentPath + "\\" + dirContent[index]
		if path.isdir(fullPath):
			removeIndexes.append(dirContent[index])
		else:
			dirContent[index] = fullPath

	for toRemove in removeIndexes:
		dirContent.remove(toRemove)

	if len(dirContent) == 0:
		return False
	else:
		
		return dirContent