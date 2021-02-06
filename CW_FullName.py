#Christopher Weiner
#CS 362 - HW4 - Full Name
def fullName(x,y):
    if(isinstance(x,int) == True):
        return "First names are not numbers"
    if(isinstance(y,int) == True):
        return "Last names are not numbers"
    tempX = str(x).strip()
    tempY = str(y).strip()
    z = tempX + " " + tempY
    return z