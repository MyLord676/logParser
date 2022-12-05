import re


class stringComparer:

    def Contains(pattern: str, compared: str):
        match = re.search(pattern, compared)
        return True if match else False

    def SplitByOrder(patternList: "list[str]", stringToSplit: str):
        allFound = True
        arr: list[str] = []
        for index, value in enumerate(patternList):
            match = re.search(value, stringToSplit)
            if match:
                arr.append(match[0])
                stringToSplit = re.sub(value, "", stringToSplit, 1)
            else:
                arr.append("")
                allFound = False
        return arr, allFound
