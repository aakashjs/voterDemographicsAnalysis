#creates a consolidated text file using individual files "AC1740001b.txt"
#consolidated text file contains data of all voters, with each line
#representing the data of single voter
'''This file contains functions for reading and writing the required files
Files to be read:
1. txt
Files to be written
1. txt
2. csv
'''

def singleVoterDataString(singleVoterDataStringTxtFileName):	
	with open(singleVoterDataStringTxtFileName,'r') as f:
		singleVoterDataString = f.readlines()

	return singleVoterDataString


def writeVoterConsolidatedDataOnTxt(pdfFileName,singleVoterDataStringList):
	fileName = "voterConsolidatedDataAsStringSample.txt"
	with open(fileName,'a') as f:
		for index,value in enumerate(singleVoterDataStringList):
			slNo = int(index)+1
			newElement = pdfFileName + "\t"+ "slNo"+str(slNo)+"\t"+ value 
			f.write(newElement)
			#f.write("\n")
	print "Voter Data String written on Consolidated file for: ", pdfFileName


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


def automate():
    numberList = generateNumberList()
    #[:3] for 3 files only, use [:] for files upto 399
    numbers = numberList[:]

    for number in numbers:
    	pdfFileName = "AC174"+ number +".pdf"
        singleVoterDataStringTxtFileName = "AC174"+ number +"b.txt"
        singleVoterDataStringList = singleVoterDataString(singleVoterDataStringTxtFileName)
        writeVoterConsolidatedDataOnTxt(pdfFileName, singleVoterDataStringList)


def main():
	automate()

if __name__ == '__main__':
	main()