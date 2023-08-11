import hashlib
import fileexplorer
import json
import click

hashDic = {}
nextDir = []
visited = []

def toJson(info):
	return json.dumps(info, indent=4)

def cleanJson(jsonPayload):
	cleanedJsonPayload = {}
	for key, value in jsonPayload.items():
		if len(jsonPayload[key]) > 1:
			cleanedJsonPayload[key] = value
	return toJson(cleanedJsonPayload)


def isInDict(hashFile):
	if hashFile in hashDic:
		return True
	return False

def addToDict(hashFile, filePath):
	hashDic[hashFile] = [filePath]
	
def updateDict(hashFile, filePath):
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

def analyzeFile(currentPath):
	files = fileexplorer.getChildrenFiles(currentPath)
	if not files:
		return False
	for file in files:
		#TODO: resolver problema de seguridad
		filehash = hashing(file)
		if isInDict(filehash):
			updateDict(filehash, file)
		else:
			addToDict(filehash, file)
	return 

def traverseStack(currentPath):
	children = fileexplorer.getChildrenFolder(currentPath)
	if children == False or areAllChildrenVisited(children):
		print("visited: " + currentPath)
		visited.append(currentPath)
		analyzeFile(currentPath)
		nextDir.pop()
		return 
	nextDir.extend(children)
	traverseStack(nextDir[-1])

def saveFile(save):
	jsonPayload = cleanJson(hashDic)
	print(save)
	saveDirectory = save + 'output.json'
	with open(saveDirectory, 'w') as data:
		data.write(str(jsonPayload))

@click.command()
@click.argument("path", type=click.Path(exists=True), required=1)
@click.option("--save", default="/", help="Where to save the output")
def start(path, save):
	click.echo(f"path {path}")
	click.echo(f"save {save}")
	initialPath = path
	try:
		fileexplorer.isValidPath(initialPath)
		initialPath = fileexplorer.getAbsolutePath(initialPath)
		nextDir.append(initialPath)
		children = fileexplorer.getChildrenFolder(initialPath)
		if children != False:  
			nextDir.extend(children)
			print("initial path" + nextDir[0])
			while len(nextDir) > 0:
				traverseStack(nextDir[-1])
			print(len(visited))
			saveFile(save)
		elif fileexplorer.getChildrenFiles(initialPath) != False:
			analyzeFile(initialPath)
			saveFile(save)
		else:
			print('No files to analyze')

	except NotADirectoryError:
		print('input a valid path')


if __name__ == '__main__':
	start()