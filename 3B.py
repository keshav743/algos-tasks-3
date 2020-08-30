n = int(input())
b = int(input())
bricks = input()
brickStrength = []
for i in bricks.split():
    brickStrength.append(int(i))
newBrickStrength = []
if(n<=2 and n>=1 and b>=1 and b<=100000 and b==len(brickStrength)):
    brickStrength.sort()
    brickStrength.reverse()
    
    def reduceBricks(n,brickStrength):
        newBrickStrength = []
        a=0
        for i in range(0,len(brickStrength)):
            if(i < n-1):
                newBrickStrength.append(brickStrength[i])
            else:
                a+=brickStrength[i]
        newBrickStrength.append(a)
        return newBrickStrength
        
    newBrickStrength = reduceBricks(n,brickStrength)    
    print(min(newBrickStrength))    
