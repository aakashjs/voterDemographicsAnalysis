#extractVoterDataAnon

import re
import csv

def extractVoterDataAsDict(singleString):
	voterData = {}
	#voterData['fileNo: '] = pdfFileName
	#voterData['slNo: '] = int(slNo)+1
	voterData['voterEPIC: '] = ''
	#voterData['voterName: '] = ''
	#voterData['relativesRelation: '] = ''
	#voterData['relativeName: '] = ''
	#voterData['house: '] = ''
	voterData['age: '] = ''
	voterData['sex: '] = ''

	m = re.search("House No\.:(.*)([\s|(A-Z)][0-9][0-9][0-9][0-9][0-9]\d+)Sex:\s(.*)Age:\s(\d+)(.*)\sName:",singleString)

	voterData['voterEPIC: '] = m.group(2)
	voterData['age: '] = m.group(4)
	voterData['sex: '] = m.group(3)
	#for x in xrange(1,8):
		#print m.group(x)
		#voterData['voterEPIC: '] = m.group(4)
		#voterData['voterName: '] = m.group(3)
		#relativesRelation = m.group(7)
		#oterData['relativesRelation: '] = relativesRelation[:-2]
		#voterData['relativeName: '] = m.group(2)
		#voterData['house: '] = m.group(1)
		#voterData['age: '] = m.group(6)
		#voterData['sex: '] = m.group(5)
			
	#print voterData
	return voterData


def singleVoterDataString(singleVoterDataStringTxtFileName):	
	with open(singleVoterDataStringTxtFileName,'r') as f:
		singleVoterDataString = f.readlines()

	return singleVoterDataString


def writeVoterDataAsCsv(voterData):	
	with open('anonVoters2.csv','a') as g:
			w = csv.writer(g)
			#w.writerow(voterData.keys())
			w.writerow(voterData.values())

	#print "VoterData written on AnonVoters.csv file"

def automatedExtraction():
	consolidatedDataFileName = "voterConsolidatedDataAsString1.txt"
	voterList = singleVoterDataString(consolidatedDataFileName)
	for index,value in enumerate(voterList):
		voterData = extractVoterDataAsDict(value)
		writeVoterDataAsCsv(voterData)
		print "Done for",index+1,"voter: ", voterData

def main():
	automatedExtraction()
		

if __name__ == '__main__':
	main()