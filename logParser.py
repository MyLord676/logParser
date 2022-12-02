from MyLibs.stringComparer import stringComparer
from MyInterfaces.logReaderInterface import logReader
from domain.patternLog import patternLog


class logParser():
    def Parse(file: logReader, patterns: "list[patternLog]"):
        tempLines: "list[str]" = []
        tempPatterns = patterns.copy()

        while True:
            Str = file.readline()
            if not Str:
                break
            tempLines.append(Str)
            #print(tempLines)

            for index, value in enumerate(tempPatterns):
                i = len(tempLines)
                if stringComparer.Contains(value.markers[i - 1], tempLines[i - 1]):
                    if len(value.markers) == i:
                        tmp = ""
                        for ind, v in enumerate(tempLines):
                            if ind <= i - 1:
                                tmp += v
                        arr, all = stringComparer.SplitByOrder(value.re, tmp)

                        yield arr, all
                        tempPatterns.remove(value)
                else:
                    tempPatterns.remove(value)

            if len(tempPatterns) == 0:
                tempLines.clear()
                tempPatterns = patterns.copy()

        file.close()
