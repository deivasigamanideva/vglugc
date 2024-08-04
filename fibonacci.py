n=int(input("enter a number :"))
a,b=0,1
sum=0
for i in range(n):
    sum=sum+a
    a,b=b,a+b   
print (sum)