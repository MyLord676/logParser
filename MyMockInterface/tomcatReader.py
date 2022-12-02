import gzip
from MyInterfaces.logReaderInterface import logReader


class gzReader(logReader):
    def __init__(self, path):
        self.file = gzip.open(path, 'rb')

    def readline(self):
        bytesLine = self.file.readline()
        if bytesLine:
            decodeLine = bytesLine.decode("utf-8")
            return decodeLine
        else:
            return None

    def close(self):
        self.file.close()
