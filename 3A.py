n = input()
count = 0

if(n.isnumeric() and int(n)>=0 and int(n)<=pow(10,100000) ):
    if(len(n)==1):
        print("0")
    else:
        x = 0
        while(len(str(n))>1):
            count+=1
            for i in str(n):
                x += int(i)
            n = x 
            x = 0
    print(count)  
