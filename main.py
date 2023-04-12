import hashlib
import fileexplorer

hashDic = {}
nextDir = []
visited = []

def isInDict(hashFile):
	if hashFile in hashDic:
		return True
	return false

def addToDict(hashFile, filePath):
	if not isInDict(hashFile):
		hashDic[hashfile] = [filePath]
	
def updateDict(hashFile, filePath):
	if(isInDict(hashFile)):
		hashDic[hashFile].append(filePath)

def hashing(filepath):
	fileexplorer.isValidFile(filepath)

	sha256 = hashlib.sha256()

	with open(filepath, 'rb') as file: 
		chunk = 0
		while chunk != b'': 
			chunk = file.read(1024)
			sha256.update(chunk)

		return sha256.hexdigest()

def areAllChildrenVisited(children):
	for child in children:
		if child not in visited:
			return False
	
	return True


# TODO: función para moverse en el stack
def traverseStack(currentPath):
	# checar que todos los folders hijo están visitados 
	children = fileexplorer.getChildrenFolder(currentPath)
	if children == False or areAllChildrenVisited(children):
		print("visited" + currentPath)
		visited.append(currentPath)
		# TODO: función para agregar hashes
		nextDir.pop()
		return 
	nextDir.extend(children)
	traverseStack(nextDir[-1])

		

def main():
	initialPath = input('Input a path\n')
	try:
		fileexplorer.isValidPath(initialPath)
		initialPath = fileexplorer.getAbsolutePath(initialPath)
		nextDir.append(initialPath)
		children = fileexplorer.getChildrenFolder(initialPath)
		nextDir.extend(children)
		print("initial path" + nextDir[0])
		while len(nextDir) > 0:
			traverseStack(nextDir[-1])
			
		#TODO: mientras se tenga algo en el stack 
		#TODO: si no tiene hijos ver si hay archivos en el camino, si no hay termina 
		print(len(visited))

	except NotADirectoryError:
		print('input a valid path')


main()