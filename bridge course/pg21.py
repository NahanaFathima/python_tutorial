#file handling
with open("example.txt","r") as f:
	print(f.read())
	
with open("example.txt",'w')as f:
	f.write("hello world")
	
with open("example.txt",'a')as f:
	f.write("\n appended line")
	
with open("example.txt")as f:
	words=f.read().split()
	print("word count:",len(words))
	
with open("example.txt")as f:
	lines=f.readlines()
	print(lines)
	print("line count:",len(f.readlines()))

with open("f1.txt")as f1, open("f2.txt")as f2:
	with open("merged.txt","w") as f3:
		f3.write(f1.read()+f2.read())


try:
	with open("nofile.txt") as f:
		print(f.read())
except FileNotFoundError:
	print("file not found")
	

	
try:
	a=10/0
except ZeroDivisionError:
	print("cannot divide by zero ")
	
	

try:
	x=int(input("enter number:"))
except ValueError:
	print("invalid error")
else:
	print("valid input")
finally:
	print("end of program")
	
	
	
with open('example.txt', 'r') as file:
    content = file.read()

reversed_content = content[::-1]

with open('example.txt', 'w') as file:
	 file.write(reversed_content)
	




with open('f1.txt', 'r') as src_file:
	content = src_file.read()

with open('f2.txt', 'w') as dest_file:
	dest_file.write(content)



















   

