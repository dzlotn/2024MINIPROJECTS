def toBinary(x):
    return bin(x)[2:]

def splitString(a):
    return [a[i:i+3] for i in range(0,len(a),3)]

def binarySequencing(code):
    return [toBinary(int(i)) for i in splitString(code)]

def insertCharCtIndicator(code):
    binList = binarySequencing(code)
    charCount = bin(len(code))[2:]
    binList.insert(0,charCount)
    return binList

 
code= "109203948"
mainBinList = binarySequencing(code)

print((insertCharCtIndicator(code)))



