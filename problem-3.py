a=int(input("enter the range:"))
if a%2==0:
    a=a-1
result=[i for i in range(1,2*a,2)]
print(result)