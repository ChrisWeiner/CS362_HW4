#Christopher Weiner
#CS 362 - HW4 - Volume of Cube
import cmath
def cubeVolume(x):
    if(isinstance(x,complex) == True):
        return "X cannot be complex"
    elif(isinstance(float(x),float) == False):
        return "X is not a valid number"
    elif(int(x) == 0):
        return "Cube cannot have zero volume"
    elif(float(x) < 0):
        return "X is less than zero"
    return x * x * x