from MyLibs.stringComparer import stringComparer
from MyInterfaces.logReaderInterface import logReader
from domain.patternLog import patternLog


class logParser():
    def Parse(logs: logReader, pattern: "patternLog"):
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
            if stringComparer.Contains(pattern.markers[i - 1],
                                       tempLines[i - 1]):
                if len(pattern.markers) == i:
                    arr, all = stringComparer.SplitByOrder(
                        pattern.re, ''.join(tempLines))

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
