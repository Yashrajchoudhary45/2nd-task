L1=[]
n=int(input("Enter the no. of elements="))
for i in range(0,n):
    ele=int(input())
    L1.append(ele)

if n%2==0:
    m1=L1[n//2]
    m2=L1[n//2-1]
    median=(m1+m2)//2
else:
    median=L1[n//2]
print('Median='+str (median))
