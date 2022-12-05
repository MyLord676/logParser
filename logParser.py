from MyLibs.stringComparer import stringComparer
from MyInterfaces.logReaderInterface import logReader
from domain.patternLog import patternLog


class logParser():
    def Parse(file: logReader, patterns: "list[patternLog]"):
        tempLines: "list[str]" = []
        tempPatterns = patterns.copy()
        send = False
        skip = False
        while True:
            if not skip:
                Str = file.readline()
                if not Str:
                    break
                tempLines.append(Str)
            else:
                skip = False

            for index, value in enumerate(tempPatterns):
                i = len(tempLines)
                if stringComparer.Contains(value.markers[i - 1], tempLines[i - 1]):
                    if len(value.markers) == i:
                        arr, all = stringComparer.SplitByOrder(
                            value.re, ''.join(tempLines))

                        yield arr, all
                        tempPatterns.remove(value)
                        send = True
                else:
                    tempPatterns.remove(value)
                    send = False

            if len(tempPatterns) == 0:
                if len(tempLines) > 1 and not send:
                    temp = tempLines.pop()
                    tempLines.clear()
                    tempLines.append(temp)
                    skip = True
                else:
                    tempLines.clear()
                tempPatterns = patterns.copy()

        file.close()
