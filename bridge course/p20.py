a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
c=int(input("enter 3rd no:"))
if a>=b and a>=c:
	print("max is:",a)
elif b>=a and b>=c:
	print("max is:",b)
else:
	print("max is:",c)
