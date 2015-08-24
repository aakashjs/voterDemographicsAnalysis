#lists.py

def generateNumberList():
	'''(NoneType) -> list
	Returns a list of numbers from "0001" to "0399"	
	'''
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


def fileNames(end):
	'''(int) -> list, list, list
	Takes the number of files in the list as input (end)
	Returns 3 lists. Each is a list of file Names
	list1 : list of pdf file Names
	list2 : list of file names converted from pdf to text
	list3 : list of fileNames after first extraction using regex
	'''
	numberList = generateNumberList()
	#[:3] for 3 files only, use [:] for files upto 399
	numbers = numberList[:end]
	pdfsNameList = []	
	txtConvertsNameList = []	
	firstExtractsNameList = []

	for number in numbers:
		pdfsNameList.append("AC174"+ number +".pdf")
		txtConvertsNameList.append("AC174"+ number +".txt")
		firstExtractsNameList.append("AC174"+ number +"b.txt")		    	

   	return pdfsNameList, txtConvertsNameList, firstExtractsNameList


def main():
	pdfsNameList, txtConvertsNameList, firstExtractsNameList = fileNames(2)
	print pdfsNameList
	print txtConvertsNameList
	print firstExtractsNameList

if __name__ == '__main__':
	main()