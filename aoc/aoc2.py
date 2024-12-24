l1 = []

#Returns if list is all increasing or decreasing
def testRule1(l1:list):
    x=[]
    decreasing = True
    inc = True
    for j in range(1,len(l1)):
        if l1[j] > l1[j-1]:
            decreasing = False
        if l1[j]<l1[j-1]:
            inc = False
    return inc or decreasing

#Returns true if line is safe with one removal
def saferemoval(l1:list):
    for i in range(len(l1)):
        modified=  l1[:i]+l1[i+1:]
        if  testRule1(modified) and  testRule2(modified): 
            return True
    return False
  
#DEPRECATED      
def r1p2(l1:list):
    x=[]
    decreasing = 0
    inc = 0
    l = len(l1)
    for j in range(1,len(l1)):
        if l1[j] > l1[j-1]:
            decreasing +=1
        if l1[j]<l1[j-1]:
            inc +=1 
    return decreasing<=1 or inc<=1

#Returns if all consecutive numbers different between 1 and 3

def testRule2(l1:list):
    for i in range(1,len(l1)):
        if abs(l1[i]-l1[i-1]) <1 or abs(l1[i]-l1[i-1])>3:
            return False
    return True

#DEPRECATED
def r2p2(l1:list):
    badCT =0
    for i in range(1,len(l1)):
        if abs(l1[i]-l1[i-1]) <1 or abs(l1[i]-l1[i-1])>3:
            badCT +=1
    return badCT<=1


# Open the file for reading
with open('aoc/aoc2.txt', 'r') as file:
    for line in file:
        values = line.strip().split()
        l1.append([int(a) for a in values])
    cp1=0
    cp2=0
    for i in l1:
        if testRule1(i) and testRule2(i):
            cp1+=1
        if saferemoval(i):
            cp2+=1
    print(cp1," ",cp2) 
        


    
    
            
    
        
        
    

