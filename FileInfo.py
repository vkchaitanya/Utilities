import os
import glob
from optparse import OptionParser

class FileInfo:
    def __init__(self, path, extension):
        self._path = path
        self._ext = extension
        self.getFileOnFileType(self._path, self._ext)

    def getFileOnFileType(self, path, extension):
        fileList = []
        for infile in glob.glob(path+extension):
            (filepath,filename) = os.path.split(infile)
            (filename,extension) = os.path.splitext(filename)
            fileList.append(filename)
        #self._displayFile(fileList)
        self._getFileCount(fileList)
        self.dumpFileName(fileList)

    def _getFileCount(self, fileList):
        print 'Total Number of files: ',len(fileList)

    def _displayFile(self, fileList):
        for f in fileList:
            print f

    def dumpFileName(self, fileList):
        f = open('imageNames.txt','a')
        for name in fileList:
            f.write(name)
            f.write('\n')

if __name__ == "__main__":
    usage = "usage: %prog [options] arg"
    options = OptionParser(usage)
    options.add_option("-l", "--filelocation", dest="location", help="input file location")
    options.add_option("-e","--extension", dest="extension", help="input file extension")
    (opts, args) = options.parse_args()
    '''print 'Given a path and the extension, this utility lets you to output the total files with that extension and a count of those files'
    path = raw_input('Enter the path name (Ex: /home/ab/folder/): ')'''
    #path = options.location
    if opts.location[-1] != '/':
        opts.location = opts.location+'/'
    f = FileInfo(opts.location, opts.extension)
