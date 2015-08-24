#voterDemographicsAnalysis.py
import extract
import lists

def main():
	pdfsNameList, txtConvertsNameList, firstExtractsNameList = lists.fileNames()
	print pdfsNameList
	print txtConvertsNameList
	print firstExtractsNameList


if __name__ == '__main__':
	main()