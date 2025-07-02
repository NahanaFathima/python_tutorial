#count vowels and consonents

s=input("enter string:")
vowels="aeiouAEIOU"
v,c=0,0
for ch in s:
	if ch.isalpha():
		if ch in vowels:
			v+=1
		else:
			c+=1
print("vowels:",v,"consonents=",c)
