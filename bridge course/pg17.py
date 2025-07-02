#charac freq in a string
s="hello"
freq={}  
for char in s:
	freq[char]=s.count(char)
print(freq)
