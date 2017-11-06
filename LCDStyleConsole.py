#Defining structure of Each Number
#Information about existence of all 8 segments
#top,top-left,top-right,center,bottom-left,bottom-right,bottom
one = [False,False,True,False,False,True,False]
two = [True,False,True,True,True,False,True]
three = [True,False,True,True,False,True,True]
four = [False,True,True,True,False,True,False]
five = [True,True,False,True,False,True,True]
six = [True,True,False,True,True,True,True]
seven = [True,False,True,False,False,True,False]
eight = [True,True,True,True,True,True,True]
nine = [True,True,True,True,False,True,True]
zero = [True,True,True,False,True,True,True]


#all structure in an array
numStructure= [zero,one,two,three,four,five,six,seven,eight,nine]

#get a 8-display first, modify it later to specific number
def get8Matrix(size):
    matRowSize = (2*size)+3
    matColSize = size+2

    horizonLine=[' ']+(['-']*size)+[' ']
    vertLine = ['|']+([' ']*size)+['|']
    
    matrix = []
    #indexes of all horizontal lines
    horzns = [0,size+1,(matRowSize-1)]
    
    for i in range(matRowSize):
        matrix.append([])
        if i in horzns:
            matrix[i]=horizonLine[:]
        else:
            matrix[i]=vertLine[:]
            
    return matrix
    

#Generate indivudual number                           
def generateNum(num,size):
    fullMatrix = get8Matrix(size)
    structure = numStructure[num]
    matRowSize = (2*size)+3
    matColSize = size+2

    
    horzClean = [' ']*size
    horzClean = [' ']+horzClean+[' ']

    #Modcify 8-seg matrix, as per number strucutre (horizontals)
    if not(structure[0]):
        fullMatrix[0]=horzClean[:]
    
    if not(structure[3]):
        fullMatrix[size+1]=horzClean[:]

    if not(structure[6]):
        fullMatrix[matRowSize-1]=horzClean[:]

    
    #Modcify 8-seg matrix, as per number strucutre (Verticals)
    for i in range(size):
        if not(structure[1]):
            fullMatrix[i+1][0]=' '

        if not(structure[2]):
            fullMatrix[i+1][matColSize-1]=' '

        if not(structure[4]):
            fullMatrix[size+2+i][0]=' '

        if not(structure[5]):
            fullMatrix[size+2+i][matColSize-1]=' '


    return fullMatrix
    

#Get all numbers into digits, and then as 8-seg matrix
#print them rowwise
def printLCD(number,size):
    allNums=[]
    while(number>0):
        digit = number%10
        number = int(number/10)
        matNum = generateNum(digit,size)
        allNums.append(matNum)

    #Reverse needed to fix
    allNums.reverse()

    lineLengthHor = len(allNums)
    lineLenthVert = len(allNums[0])

    #Horizontal printing
    for i in range(lineLenthVert):
        for numMat in allNums:
            line = numMat[i]
            for char in line:
                print(char,end='')
            print(' ',end='')
        print()



printLCD(12345,1)
    

        
