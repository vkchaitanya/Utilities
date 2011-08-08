import os
import glob

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
        self._displayFile(fileList)
        self._getFileCount(fileList)

    def _getFileCount(self, fileList):
        print 'Total Number of files: ',len(fileList)

    def _displayFile(self, fileList):
        for f in fileList:
            print f

if __name__ == "__main__":
    print 'Given a path and the extension, this utility lets you to output the total files with that extension and a count of those files'
    path = raw_input('Enter the path name (Ex: /home/ab/folder/): ')
    if path[-1] != '/':
        path = path+'/'
    ext = raw_input('Enter the extension (Ex: *.pdf): ')
    f = FileInfo(path, ext)
