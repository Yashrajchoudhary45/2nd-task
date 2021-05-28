n=int(input('enter a no.='))
for y in range(1,n+1,1):
    n=y
    count=0
    for x in range(1,n+1,1):
        if(n%x==0):
            count=count+1
    if count==2:
        print(n,end=",")
