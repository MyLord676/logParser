from MyLibs.stringComparer import stringComparer
from MyInterfaces.logReaderInterface import logReader
from domain.patternLog import patternLog


class logParser():
    def Parse(logs: logReader, patterns: "list[patternLog]"):
        tempLines: "list[str]" = []
        tempPatterns = frozenset(patterns.copy())
        send = False
        skip = False
        while True:
            if not skip:
                Str = logs.readline()
                if not Str:
                    break
                tempLines.append(Str)
            else:
                skip = False

            remove: "list[patternLog]" = []
            for value in tempPatterns:
                i = len(tempLines)
                if stringComparer.Contains(value.markers[i - 1],
                                           tempLines[i - 1]):
                    if len(value.markers) == i:
                        arr, all = stringComparer.SplitByOrder(
                            value.re, ''.join(tempLines))

                        yield arr, all
                        remove.append(value)
                        send = True
                else:
                    remove.append(value)
                    send = False

            tempPatterns = [item for item in tempPatterns if
                            item not in remove]
            remove.clear()

            if len(tempPatterns) != 0:
                continue

            tempPatterns = patterns.copy()

            if len(tempLines) > 1 and not send:
                temp = tempLines.pop()
                tempLines.clear()
                tempLines.append(temp)
                skip = True
            else:
                tempLines.clear()

        logs.close()
