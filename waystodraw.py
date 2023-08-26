import math
frequencies=[9,2,2,4,12,2,3,4,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1,1]
letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",r"\n"]
inputFile="/Users/etbrosowsky/Zyzzyva/words/saved/SevenAlphagrams.txt"
rack=""
freqIndex=0
overallDraws=math.comb(98,7)
waysToDraw=1
lineQuant=21068
finalDraw=[]

with open(inputFile, 'r') as filedata:
    linesList= filedata.readlines()
    finalLine=[]
    for textline in (linesList[:lineQuant]):
        finalLine.append(textline.strip())
    for i in (finalLine[:lineQuant]):
        rack=i
        for i in rack:
            freqIndex=letters.index(i)
            if rack.count(i)>1:
                multip=math.comb(frequencies[freqIndex],rack.count(i))**(1/rack.count(i))
                waysToDraw*=multip
            else : 
                multip=math.comb(frequencies[freqIndex],rack.count(i)) 
                waysToDraw*=multip
        finalDraw.append(round(waysToDraw))
        waysToDraw=1
filedata.close()
totalDraws=sum(finalDraw)
print(totalDraws)
print(overallDraws)
print(totalDraws/overallDraws)