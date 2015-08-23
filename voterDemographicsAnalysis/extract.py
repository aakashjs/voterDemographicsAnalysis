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
	#this regex extracts almost correctly
	#m = re.search("House No\.:(.*)([\s|(A-Z)][0-9][0-9][0-9][0-9][0-9]\d+)Sex:\s(.*)Age:\s(\d+)(.*)\sName:",singleString)
	#regex2
	#m = re.search("House No\.:(.*)((\s|[A-Z]{3,3})[0-9][0-9][0-9][0-9][0-9]\d+)Sex:\s(.*)Age:\s(\d+)(.*)\sName:",singleString)
	#regex3
	m = re.search("House No\.:(.*)(\s.*)Sex:\s(.*)Age:\s(\d+)(.*)\sName:",singleString)
	#regex4
	#m = re.search("House No\.:(.*)((\s|[A-Z]{3,3}|[A-Z]{3,3}.*[\d+])[0-9][0-9][0-9][0-9][0-9]\d+)Sex:\s(.*)Age:\s(\d+)(.*)\sName:",singleString)


	#voterData['voterEPIC: '] = m.group(2)
	voterData['sex: '] = m.group(3)
	voterData['age: '] = m.group(4)	
	#for x in xrange(1,8):
		#print m.group(x)	
	#voterData['voterName: '] = m.group(3)
	#relativesRelation = m.group(7)
	#oterData['relativesRelation: '] = relativesRelation[:-2]
	#voterData['relativeName: '] = m.group(2)
	#voterData['house: '] = m.group(1)
	
			
	#print voterData
	return voterData


def singleVoterDataString(singleVoterDataStringTxtFileName):	
	with open(singleVoterDataStringTxtFileName,'r') as f:
		singleVoterDataString = f.readlines()

	return singleVoterDataString


def writeVoterDataAsCsv(voterData):
	pathCsv = "E:/myProjects/gitRepos/voterDemographicsAnalysis/reports/"
	csvFileName = "anonVoters2.csv"
	csvFilePathName = pathCsv + csvFileName
	with open(csvFilePathName,'a') as g:
			w = csv.writer(g)
			#w.writerow(voterData.keys())
			w.writerow(voterData.values())

	#print "VoterData written on AnonVoters.csv file"

def automatedExtraction():
	pathTextFile = "E:/myProjects/gitRepos/voterDemographicsAnalysis/sampleFiles/voterDataExtracted/"
	consolidatedDataFileName = "voterConsolidatedDataAsStringSample2.txt"
	consolidatedDataFilePathName = pathTextFile+consolidatedDataFileName
	voterList = singleVoterDataString(consolidatedDataFilePathName)
	for index,value in enumerate(voterList):
		voterData = extractVoterDataAsDict(value)
		writeVoterDataAsCsv(voterData)
		print "Done for",index+1,"voter: ", voterData

def main():
	automatedExtraction()
		

if __name__ == '__main__':
	main()