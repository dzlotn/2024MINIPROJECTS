class QR:
    def toBinary(x):
        return bin(x)[2:]
    
    def splitString(a):
        return [a[i:i+3] for i in range(0,len(a),3)]
    
    #creates binary list from data 
    def binarySequencing(code):
        return [QR.toBinary(int(i)) for i in QR.splitString(code)]
    
    #adds mode indactor to qr based on version
    def modeIndicator(type):
        d = {"ECI":"0111","Numeric":"0001","Alphanumeric": "0010","Byte":"0100","Kanji":"1000","Structured Append":"0011"}
        try:
            return d[type]
        
        except KeyError:
            print("Incorrect Mode Type Selected")
            quit()
        
    #creates final bit string  
    def encodeData(code,mode):
        m = QR.modeIndicator(mode)
        binList = QR.binarySequencing(code)
        charCount = bin(len(code))[2:]
        binList.insert(0,charCount)
        binList.insert(0,m)
        return binList

    
code= "01234567"
mainBinList = QR.binarySequencing(code)

print((QR.encodeData(code,"ECI")))



