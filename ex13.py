from sys import argv

script, first, second, third, fourth = argv
print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is", third)


# Script with 6 arguments

script, name1, name2, name3, name4, name5 = argv

print ("The script name is" ,script,".\nThe first of the group is" 
	,name1,".\nThe second is" ,name2,".\nThe third is",name3,".\nThe fourth is" 
	,name4,".\n And the latter is",name5,".")


# script with argv and input

script, profession = argv
print ("This script name is", script, "and it will ask you as a", profession, "about your personal data")

your_name = input("What is your name? ")
birth_city = input("Where where you born? ")
birth_year = int(input("In what year? "))
job = profession
age = 2018 - birth_year

print ("So you're %s, you were born in %s and your %r years old, currenty a %s" % (your_name, birth_city, age, job))



# script with input 

print ("This script name is exand it will ask you about your personal data")
script, your_name, birth_city, age, job = argv

your_name = input("What is your name? ")
birth_city = input("Where where you born? ")
birth_year = int(input("In what year? "))
profession = input("What is your professon? ")
job = profession
age = 2018 - birth_year

print ("This script name is", script, "So you're %s, you were born in %s and your %r years old, currenty a %s" 
	% (your_name, birth_city, age, job))



# input and argv combined

print ("This script name is exand it will ask you about your personal data")

name = input(your_name)
city = input(birth_city)
year = input(birth_year)

script, name, city, year = argv

print ("This script name is" ,script, "So you're %s, you were born in %s at %s" 
	% (name, city, year))
