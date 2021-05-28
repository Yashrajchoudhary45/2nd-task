a=int(input('enter a no.='))
b=int(input('enter a no.='))
c=int(input('enter a no.='))
count=1
if(a==b):
    if(b!=c):
        count+=1
    else:
        count+=2
elif(b==c):
    if(c!=a):
        count=count+1
    
elif(c==a):
    if(a!=b):
        count+=1
    
else:
    count=0
print(count)
