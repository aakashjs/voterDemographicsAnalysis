#downloadPdfs.py

import os
import urllib2
import time
import shutil

def downloadPdf(pdfUrl,downloadedPdfName):
    print "File Download Started for: ", downloadedPdfName
    path = 'E:/myProjects/gitRepos/voterDemographicsAnalysis/sampleFiles/pdfs/'
    #path = '../sampleFiles/samplePdfs/'
    response = urllib2.urlopen(pdfUrl)
    file = open(downloadedPdfName, 'wb')
    file.write(response.read())
    file.close()
    shutil.move(downloadedPdfName, path+downloadedPdfName)
    print "File Download Completed for: ", downloadedPdfName


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

        
def automatedDownload():
    numberList = generateNumberList()
    #[:3] for 3 files only, use [:] for files upto 399
    numbers = numberList[:2]
    for number in numbers:
        pdfUrl = "http://ceokarnataka.kar.nic.in/FinalRoll_2015/English/WOIMG/AC174/AC174"+ number +".pdf"
        downloadedPdfName = pdfUrl[-13:-3]+"pdf"        
        downloadPdf(pdfUrl,downloadedPdfName)
        print "waiting for 30 seconds before downloading next file:"
        #uncomment the for loop if waiting not required        
        for x in xrange(1,31):            
            print x,",",
            time.sleep(1)
        print "\n"            
        #uncomment next 5 lines if you want to delete the downloaded pdf & extracted txt files
        #path = 'E:/../path/to/pdfs'
        #downloadedPdfPath = path + downloadedPdfName
        #convertedTextFilePath = path + firstPageTextFileName
        #os.remove(downloadedPdfPath)
        #os.remove(convertedTextFilePath)


def main():
    automatedDownload()

if __name__ == '__main__':
    main()