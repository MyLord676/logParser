import gzip
import stringComparer


def main():
    i = 0
    order = [
            "\d{1,2}-\w{3}-\d{4}", 
            "\d{1,2}:\d{1,2}:\d{1,2}.\d{1,3}",
            "\d{1,4}",
            "\d*ms",
            ]
    with gzip.open('tomcat.log.gz', 'rb') as fin:
        bytesRead: bytes
        while True:
            bytesRead = fin.readline()
            if not bytesRead:
                break
            i += 1
            firstStr = bytesRead.decode("utf-8")
            warning = stringComparer.Contains("WARNING", firstStr)
            if not warning:
                continue
            bytesRead = fin.readline()
            if not bytesRead:
                break
            SecondStr = bytesRead.decode("utf-8")
            elapsed = stringComparer.Contains("ELAPSED", SecondStr)
            if not elapsed:
                continue
            arr, all = stringComparer.SplitByOrder(order, firstStr + SecondStr)
            print(arr, all)

    fin.close()
    print(i)


if __name__ == '__main__':
    main()
