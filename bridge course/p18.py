n=int(input("enter a no:"))
count=0
while n>0:
	n//=10
	count +=1
print("no of digits:",count)
n=input()
print(len(n))
