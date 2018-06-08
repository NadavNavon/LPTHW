# x is a (str) variable with the int 10 converted into str inside it
x = "There are %d types of people." % 10
#str variable
binary = "binary"
#str variable
do_not = "don't"
#str variable with two str variables inside it
y = "Those who know %s and those who %s." % (binary, do_not)

#printing (str) variable
print (x)
#printing (str) variable with two (str) variables inside it
print (y)

#printing a (str) with a (str) variable inside it
print ("I said: %r." % x)
print ("I also said: '%s'." % y)

#This is a bull variable. True/False = bull.
hilarious = True

#This is a (str) variable, which is ready to accept a format character
joke_evaluation = "Isn't that joke so funny?! %r"

#printing the (str) variable with a format character variable
print (joke_evaluation % hilarious)

#string variables
w = "This is the left side of..."
e = "a string with a right side."

print (w + e)

