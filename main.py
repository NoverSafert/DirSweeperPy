import hashlib
import fileexplorer

def hashing(filepath):
	fileexplorer.isValidFile(filepath)

	sha256 = hashlib.sha256()

	with open(filepath, 'rb') as file: 
		chunk = 0
		while chunk != b'': 
			chunk = file.read(1024)
			sha256.update(chunk)

		return sha256.hexdigest()

def compare(file1, file2):
	hash1 = hashing(file1)
	hash2 = hashing(file2)
	print(hash1)
	print(hash2)

	if hash1 == hash2:
		print("same content")

def main():
	docx1 = './tests/docs/doc1.docx'
	docx2 = './tests/docs/doc1 (copy).docx'
	odt1 = './tests/docs/doc1.docx'
	odt2 = './tests/docs/doc1 (copy).docx'
	img1 = './tests/images/image1'
	img2 = './tests/images/image1 (copy)'
	pdf1 = './tests/pdfs/doc1.pdf'
	pdf2 = './tests/pdfs/doc1 (copy).pdf'
	txt1 = './tests/txt/doc1.txt'
	txt2 = './tests/txt/doc1 (copy).txt'
	
	compare(docx1, docx2)
	compare(odt1, odt2)
	compare(img1, img2)
	compare(pdf1, pdf2)
	compare(txt1, txt2)

	fileexplorer.hasChildren(img1)

main()