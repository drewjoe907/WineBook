#! python
import nltk, re
import PyPDF2

pdfFileObj = open('wine_list.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(38)
page38 = pageObj.extractText()
p38 = page38.encode('utf-8')
a = p38.split('\n')


def search(args):
	if args in a:
		print a[a.index(args)], a[a.index(args)+1], a[a.index(args)+9]
	else:
		print 'not found'
