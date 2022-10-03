
def convert(textFile,split = "\n"):
    """Converts to a list of strings"""
    string = open(textFile).read()
    strList = string.split(split)
    return strList

def convertToInt(textFile):
    string = open(textFile).read()
    strList = string.split("\n")
    return [int(strList[i]) for i in range(len(strList))]