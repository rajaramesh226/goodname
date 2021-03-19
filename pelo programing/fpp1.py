x=int(input("enter the number"))
for i in range(2,x+1):
	if(x%i==0):
		print(i,"is a divisor of",x)