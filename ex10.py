tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies 
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

print ('a"\t"b')
print ("a"  "b")

print ("")

print ("I am 5'7\" tall.") # escape the double-quote inside string
print ('I am 5\'7" tall.') # escape the single-quote inside string
print ("")
print ("how are you %r" % "john")
print ("how are you \'%r\' " % "john")
print ('how are you \"%r\" ' % 'john')

print ("")
print ("how are you %s" % "john")
print ("how are you \'%s\' " % "john")
print ('how are you \"%s\" ' % 'john')

print ("")
print ("How much is \"Willy\" weight? %s \nAnd how much \"Dambo\"? %s" % ("1000 pounds.", "500 pounds."))