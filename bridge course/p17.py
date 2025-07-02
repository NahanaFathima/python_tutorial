num= int(input("enter a no:"))
rev=0
while num!=0:
	rev=rev*10+num%10
	num//=10
print("reversed no:",rev)



num=input()
print(num[::-1])
