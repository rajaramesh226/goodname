str=input("Enter a Word or a String-")
print(str[0:len(str)])
str1=str[::-1]
print(str1)
if(str[0:len(str)]==str[::-1]):
	print("pal")
else:
	print("not pal")