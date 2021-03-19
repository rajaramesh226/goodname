a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for j in b:
 if j in a:
 	continue
    
 else:
	a.append(j)
a=set(a)
a1=[] # empty list creation
for i in a:
 a1.append(i)
a1.sort()
print(a1)