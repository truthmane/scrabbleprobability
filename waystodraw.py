import math
frequencies=[9,2,2,4,12,2,3,4,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]
letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
rack="AEINRST"
freqIndex=0
waystodraw=1

for i in rack:
    freqIndex=letters.index(i)
    if rack.count(i)>1:
        multip=math.comb(frequencies[freqIndex],rack.count(i))**(1/rack.count(i))
        waystodraw*=multip
    else : 
        multip=math.comb(frequencies[freqIndex],rack.count(i)) 
        waystodraw*=multip
print(round(waystodraw))

