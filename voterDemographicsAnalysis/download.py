#downloadPdfs.py

import os
import urllib2
import time
import shutil
import lists

def downloadPdf(pdfUrl,pdfFileName):
    print "File Download Started for: ", pdfFileName
    path = 'E:/myProjects/gitRepos/voterDemographicsAnalysis/sampleFiles/pdfs/'
    #path = '../sampleFiles/samplePdfs/'
    response = urllib2.urlopen(pdfUrl)
    file = open(pdfFileName, 'wb')
    file.write(response.read())
    file.close()
    shutil.move(pdfFileName, path+pdfFileName)
    print "File Download Completed for: ", pdfFileName

       
def automatedDownload(startIndex,endIndex):
    '''(NoneType) -> NoneType
    Takes the name from the urlList and download that file
    '''
    urls = lists.urlsList(startIndex,endIndex)
    for url in urls:
        pdfFileName = url[-13:-3]+"pdf"
        downloadPdf(url, pdfFileName)
        print "waiting for 30 seconds before downloading next file:"
        #uncomment the for loop if waiting not required        
        for x in xrange(1,31):            
            print x,",",
            time.sleep(1)
        print "\n"
        #uncomment next 5 lines if you want to delete the downloaded pdf & extracted txt files
        #path = 'E:/../path/to/pdfs'
        #downloadedPdfPath = path + pdfFileName
        #convertedTextFilePath = path + firstPageTextFileName
        #os.remove(downloadedPdfPath)
        #os.remove(convertedTextFilePath)


def main():
    automatedDownload(6,7)

if __name__ == '__main__':
    main()