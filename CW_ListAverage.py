#Christopher Weiner
#CS 362 - HW4 - List Average

def listAverage(x):
    listSum = sum(x)
    listLength = len(x)
    if(listLength == 0):
        return "There are zero elements in the list"
    else:
        return listSum/listLength