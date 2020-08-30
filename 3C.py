import math

n = int(input())
if(n>=2 and n<=100000):
    arr = []
    samArr = []
    arr2 = []
    finalArr = []
    for i in range(2,n+1):
        arr.append(i)
    g2 = []
    g3 = []
    g5 = []
    g7 = []
    finalArr = []
    
    for i in arr:
        if(i%2==0):
            g2.append(i)
        elif(i%3==0):
            g3.append(i)
        elif(i%5==0):
            g5.append(i)
        elif(i%7==0):
            g7.append(i)    
    
    for i in arr:
        if(not(i in g2 or i in g3 or i in g5 or i in g7)):
            samArr.append(i)
    
    for i in samArr:
        for j in samArr:
            if(i<j and j%i==0):
                arr2.append(i) 
                arr2.append(j)
                
    arr2 = set(arr2)
    
    for i in arr2:
        if(i in samArr):
            samArr.remove(i)
            
    arr2= list(arr2)
    arr2.sort()
    
    facArr = []
    
    for i in range(0,math.ceil(len(arr2)/2)):
        s=[]
        for j in arr2:
            if((not arr2[i]==j) and j%arr2[i]==0):
                s.append(arr2[i])
                s.append(j)
        s=set(s)
        s=list(s)
        if(not len(s)==0):    
            facArr.append(s)
        
    finalArr = [g2]+[g3]+[g5]+[g7]+[facArr]+[samArr]    
    
    count = 0
    t = 1
    for i in range(0,6):
        if(i<4):
            if(not len(finalArr[i])==0):
                count+=(i+1)
                t+=1
        elif(i==4):
            if(not len(finalArr[i])==0):
                for j in range(0,len(finalArr[i])):
                    count+=(j+5)
                    t+=1
        else:
            if(not len(finalArr[i])==0 and not len(finalArr[4])==0):
                for j in range(0,len(samArr)):
                    count+=(j+t)
            elif(not len(finalArr[i])==0 and len(finalArr[4])==0):
                for j in range(0,len(samArr)):
                    count+=(j+5)
    print(count)            
            
