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


def createConsolidatedTxt(startFileNumber, endingFileNumber):
    '''(str, list) -> NoneType
    Writes the voter data from each individual voter data file to a 
    consolidated file. Each voter entry contains
    1. pdfFileName from which it was extracted
    2. serial number of that voter in that pdf
    3. extracted raw voter data string (House No.:.Eshwarappa Venkatalakshmi SVF5421417Sex: FemaleAge: 31Husband's Name:)
    '''
    
    path = "E:/myProjects/gitRepos/voterDemographicsAnalysis/sampleFiles/firstExtracts/consolidated/"
    outputFileName = "firstExtractsConsolidated6.txt"

    list1 = lists.firstExtractsNamesList(startFileNumber, endingFileNumber)

    with open(path+outputFileName,'a') as f:
        for file in list1:
            pdfFileName = file[:-5]+".pdf"

            list2 = singleFileVoterData(file)

            for index,value in enumerate(list2):
                slNo = int(index)+1
                newElement = pdfFileName + "\t"+ "slNo"+str(slNo)+"\t"+ value
                f.write(newElement)
                #f.write("\n")

            print "Voter Data written on Consolidated Txt file for: ", file


def main():    
    #createConsolidatedTxt(0,2)


if __name__ == '__main__':
	main()