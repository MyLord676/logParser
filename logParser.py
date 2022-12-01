import gzip
import re


def main():
    i = 0
    with gzip.open('tomcat.log.gz', 'rb') as fin:
        bytesRead = fin.readline()
        while bytesRead:
            i += 1
            firstStr = bytesRead.decode("utf-8")

            matchFirstStr = re.search("\d{1,2}-\w{3}-\d{4} \d{1,2}:\d{1,2}:"\
                                      "\d{1,2}.\d{1,3}\sWARNING\s\[http-nio-\d*-exec-\d*\]", firstStr)
            if matchFirstStr:
                print(matchFirstStr[0])
                bytesRead = fin.readline()
                if bytesRead:
                    SecondStr = bytesRead.decode("utf-8")
                    matchSecondStr = re.match("[*]{2}\sRequest\shad\sdb\sELAPSED\stime\sof\s:\d*", SecondStr)
                    if matchSecondStr:
                        print(matchSecondStr[0])
                else:
                    return

            bytesRead = fin.readline()
    fin.close()
    print(i)


if __name__ == '__main__':
    main()
