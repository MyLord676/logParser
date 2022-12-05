from MyLibs.stringComparer import stringComparer
from MyInterfaces.logReaderInterface import logReader


class logParser():
    def Parse(logs: logReader, markers: "list[str]", re: "list[str]"):
        tempLines: "list[str]" = []
        skip = False
        while True:
            if not skip:
                Str = logs.readline()
                if not Str:
                    break
                tempLines.append(Str)

            skip = False

            i = len(tempLines)
            if stringComparer.Contains(markers[i - 1],
                                       tempLines[i - 1]):
                if len(markers) == i:
                    arr, all = stringComparer.SplitByOrder(
                        re, ''.join(tempLines))

                    yield arr, all
                    tempLines.clear()
                    continue
            else:
                if len(tempLines) > 1:
                    skip = True
                    temp = tempLines.pop()
                    tempLines.clear()
                    tempLines.append(temp)

        logs.close()
