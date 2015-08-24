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
	list3 : list of file Names after first extraction using regex
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


def pdfsNamesList(startIndex, endIndex):
	'''(int, int) -> list
	Takes the number of files in the list as input (start, end)
	Returns list of pdf file Names
	'''
	numberList = generateNumberList()
	#[:3] for 3 files only, use [:] for files upto 399
	numbers = numberList[startIndex:endIndex]
	list = []

	for number in numbers:
		list.append("AC174"+ number +".pdf")		

   	return list


def txtConvertsNamesList(startIndex, endIndex):
	'''(int, int) -> list
	Takes the number of files in the list as input (start, end)
	Returns list of file names converted from pdf to text
	'''
	numberList = generateNumberList()	
	numbers = numberList[startIndex:endIndex]
	list = []		

	for number in numbers:
		list.append("AC174"+ number +".txt")

   	return list


def firstExtractsNamesList(startIndex, endIndex):
	'''(int, int) -> list
	Takes the number of files in the list as input (start, end)
	Returns list of file Names after first extraction using regex
	'''
	numberList = generateNumberList()	
	numbers = numberList[startIndex:endIndex]
	list = []		

	for number in numbers:
		list.append("AC174"+ number +"b.txt")

   	return list


def urlsList(startIndex,endIndex):	
	l = pdfsNamesList(startIndex,endIndex)	
	list = []
	pdfUrl = "http://ceokarnataka.kar.nic.in/FinalRoll_2015/English/WOIMG/AC174/"
	
	for pdfFileName in l:
		list.append(pdfUrl+pdfFileName)

	return list


def main():
	#pdfsNamesList, txtConvertsNamesList, firstExtractsNamesList = fileNames(2)
	l1 = pdfsNamesList(0,3)
	l2 = txtConvertsNamesList(0,3)
	l3 = firstExtractsNamesList(0,3)
	l4 = urlsList(0,3)
	print l1
	print l2
	print l3
	print l4

if __name__ == '__main__':
	main()