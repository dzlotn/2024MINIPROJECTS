import numpy as np 
import random

class QR:
    @staticmethod
    def toBinary(x) -> str:
        return bin(x)[2:]
    
    @staticmethod
    def splitString(a) -> list:
        return [a[i:i+3] for i in range(0,len(a),3)]
    
    @staticmethod
    def binarySequencing(code) -> list:
        return [QR.toBinary(int(i)) for i in QR.splitString(code)]
    
    @staticmethod
    def modeIndicator(type) -> str:
        d = {"ECI":"0111","Numeric":"0001","Alphanumeric": "0010","Byte":"0100","Kanji":"1000","Structured Append":"0011"}
        try:
            return d[type]
        except KeyError:
            print("Incorrect Mode Type Selected")
            quit()
        
    @staticmethod
    def encodeData(code, mode) -> list:
        m = QR.modeIndicator(mode)
        binList = QR.binarySequencing(code)
        charCount = bin(len(code))[2:].zfill(8)  # Padding length to make it 8 bits long
        binList.insert(0, charCount)
        binList.insert(0, m)
        return binList

    def __init__(self, version:int, encodeMode:str, code:str) -> None:
        self.version = version
        self.mode = encodeMode
        self.size = 4 * version + 17
        self.code = code
        self.arr = np.zeros((self.size, self.size))
        self.encodeData("128348728374", encodeMode)
        
    def setBitColor(self, x:int, y:int, color:int) -> None:
        self.arr[x][y] = color

code = "76398659789879"

newQR  = QR(1, "ECI",code)
print(newQR.encodeData(newQR.code,newQR.mode))


# mainBinList = QR.binarySequencing(code)
# print((QR.encodeData(code,"ECI")))

# mainBinList = QR.binarySequencing(code)
# print((QR.encodeData(code,"ECI")))


arr = np.zeros((3,3),)

#QR testing
for i in range(3):
    for j in range(3):
        arr[i][j] = random.randrange(2)
print(f"{arr}")
print(arr>0)
print(arr[0][1])


