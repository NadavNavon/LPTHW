from sys import argv

# argv is setting the script to recieve inputs from the command line. In this case- 1 variable.
script, filename = argv

# #  txt is a variable calling a the function "open". The variable is equal to the open file.
# txt = open(filename)

# print ("Here's your file %r:" % filename)  # standard print command presenting the file name.
# print (txt.read()) # print the function read. 

print ("Type the filename again:") # standard print command.
file_again = (input("> ")) # the variable will be equal for the inserted input. 

txt_again = open(file_again) # txt_again is a variable calling the function "open".

print (txt_again.read()) # print the output of the command "read".

finish = txt_again.close()

###################################################################

# This is one way to open a file and than print it. 
f = open("sample.txt", 'r')
g = f.read()
print (g)
f.close()
print ("\n")

# This is a way to open a file with a "for" loop instead of calling in variables. 
f = open("sample.txt", 'r')
for line in f:
	print (line, end = '')
f.close()  #In this case as well, file must be closed unless using "with" function
print ("\n")

# ################################################################

# This is a way to open a file with a "for" loop and "with" command,  no need to for .close
with open("sample.txt", 'r') as f:
	for line in f:
		print (line, end ='')

#################################################################

# These are ways to open a file using a "with" command, "while" loops and read/readlines commands

with open('sample.txt', 'r') as f:
	size = 35
	rf = f.readlines(size)  # Read the line that reach 35 chatacters 
	while len(rf) > 0:
		print (rf, end = "*")
		rf = f.readlines(size)

print ('\n')

with open('sample.txt', 'r') as f:
	size = 10
	rf = f.read(size)
	while len(rf) > 0:
		print (rf, end = '*')
		rf = f.read(size)

#################################################################









