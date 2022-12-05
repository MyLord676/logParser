from MyMockInterface.tomcatReader import gzReader
from MyLibs.logParser import logParser
from domain.patternLog import patternLog


def main():
    pattern = [
                patternLog(
                    ["WARNING",
                     "ELAPSED"],
                    ["\d{1,2}-\w{3}-\d{4}", 
                     "\d{1,2}:\d{1,2}:\d{1,2}.\d{1,3}",
                     "\d{1,4}",
                     "\d*ms", ])
              ]
    i = 0
    for arr, all in logParser.Parse(gzReader("tomcat.log.gz"), pattern):
        print(arr, all)
        i += 1

    print(i)


if __name__ == '__main__':
    main()
