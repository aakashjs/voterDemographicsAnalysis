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
import voterDemographicsAnalysis
import lists

def singleFileVoterData(firstExtractFileName):
    '''(str) -> list
    Takes the name of the file from the firstExtractsNameList and
    Returns a list whose each element is a voter entry (like this:)
    (House No.:.Eshwarappa Venkatalakshmi SVF5421417Sex: FemaleAge: 31Husband's Name:) 
    
    '''
    path = "E:/myProjects/gitRepos/voterDemographicsAnalysis/sampleFiles/firstExtracts/"
    with open(path+firstExtractFileName,'r') as f:
		singleFileVoterData = f.readlines()
    return singleFileVoterData


def writeVoterConsolidatedDataOnTxt(firstExtractFileName):
    '''(str, list) -> NoneType
    Writes the voter data from each individual voter data file to a 
    consolidated file. Each voter entry contains
    1. pdfFileName from which it was extracted
    2. serial number of that voter in that pdf
    3. extracted raw voter data string like this:
    (House No.:.Eshwarappa Venkatalakshmi SVF5421417Sex: FemaleAge: 31Husband's Name:)
    '''
    pdfFileName = firstExtractFileName[:-5]+".pdf"
    path = "E:/myProjects/gitRepos/voterDemographicsAnalysis/sampleFiles/firstExtracts/consolidated/"
    fileName = "firstExtractsConsolidated4.txt"
    singleFileVoterDataAsList = singleFileVoterData(firstExtractFileName)
    with open(path+fileName,'a') as f:
		for index,value in enumerate(singleFileVoterDataAsList):
			slNo = int(index)+1
			newElement = pdfFileName + "\t"+ "slNo"+str(slNo)+"\t"+ value 
			f.write(newElement)
			#f.write("\n")
    print "Voter Data written on Consolidated Txt file for: ", firstExtractFileName


def main():    
    tillFileNumber = 2
    pdfsNameList, txtConvertsNameList, firstExtractsNameList = lists.fileNames(tillFileNumber)
    
    for file in firstExtractsNameList:        
        writeVoterConsolidatedDataOnTxt(file)

if __name__ == '__main__':
	main()