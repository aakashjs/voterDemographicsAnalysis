#converts pdf to text file using slate library in python
#also extracts the voter data and save it as another file with suffix fileName+"b.txt"

import slate
import re


def pdf2TxtUsingSlate(downloadedPdfName):
    inputFileName = downloadedPdfName 
    textFileName = downloadedPdfName[:-3]+"txt"
    pathPdf = "E:/path/to/pdfs/"
    with open(pathPdf+downloadedPdfName) as f:
        convertedTxt = slate.PDF(f)
    #print convertedTxt
    pathText = "E:/path/for/saving/textFiles/"
    with open(pathText+textFileName,"w") as f:
    	for element in convertedTxt:
	        f.write(element)
	print "File converted to txt using slate"
    return convertedTxt

def extractVotersPageWiseAsList(convertedTxt):
	votersPageWiseAsList = []
	for index, value in enumerate(convertedTxt):
		page = value
		#print value
		m = re.search("Continued(\d+.*)Page\s",value)
		if m:
			#print m.groups(1)
			totalVoters = m.groups(1)
			votersPageWiseAsList.append(totalVoters[0])
	print "Voters Data extracted as pagewise list "
	#print votersPageWiseAsList
	return votersPageWiseAsList


def extractSingleVoterDataStringAsList(votersPageWiseAsList):
	singleVoterDataString = []
	for index,value in enumerate(votersPageWiseAsList):
		#print value
		m = re.split("\d+Name :",value)
		#print m
		for index,value in enumerate(m):
			if value != '':
				singleVoterDataString.append(value)
		
	print "single Voter DataString extracted as list \n"
	#print singleVoterDataString
	return singleVoterDataString


def writeSingleVoterDataStringAsTxt(singleVoterDataString,downloadedPdfName):
	textFileName = downloadedPdfName[:-4]+"b.txt"
    pathText = "E:/path/for/saving/textFiles/"
	with open(pathText+textFileName,"w") as f:
		for element in singleVoterDataString:
			f.write(element)
			f.write("\n")
	print "single Voter Data String written on txt file"


def generateNumberList():
    numberList = []
    for x in xrange(1,400):
        s = str(x)
        #print s
        if x in xrange(1,10):
            number = "000" + s
            numberList.append(number)

        if x in xrange(10,100):
            number = "00" + s
            numberList.append(number)

        if x in xrange(100,400):
            number = "0" + s
            numberList.append(number)

    return numberList


def automatedExtraction():
    numberList = generateNumberList()
    #[:3] for 3 files only, use [:] for files upto 399
    numbers = numberList[:]

    for number in numbers:
        downloadedPdfName = "AC174"+ number +".pdf"        
        convertedTxt = pdf2TxtUsingSlate(downloadedPdfName)
        votersPageWiseAsList = extractVotersPageWiseAsList(convertedTxt)
        singleVoterDataString = extractSingleVoterDataStringAsList(votersPageWiseAsList)
        writeSingleVoterDataStringAsTxt(singleVoterDataString,downloadedPdfName)
        print downloadedPdfName
        print "Done"
        #uncomment next 5 lines if you want to delete the downloaded pdf & extracted txt files
        #path = 'E:/myProjects/webScrapingAssignment/virtual/venv/Scripts/'
        #downloadedPdfPath = path + downloadedPdfName
        #convertedTextFilePath = path + convertedTextFileName
        #os.remove(downloadedPdfPath)
        #os.remove(convertedTextFilePath)


def main():
	automatedExtraction()
	

if __name__ == '__main__':
	main()