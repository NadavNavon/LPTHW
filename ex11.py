#!/usr/bin/env python

# This command ask a question using a (str) and waits for a replay
print ("How old are you?"),
age = int(input())
print ("How tall are you?"),
height = input()
print ("How much do you weigh?"),
weight = input()

print ("So, you're %r old, %r tall and %r heavy." % (
	age, height, weight))


print (type(age))
print (type(height)) 
print (type(weight))
# This is how NOT to do it 
#1. print ("how old are you?", input())

#2. a = input()
#   print ("hey you", a)

name = input('enter your name: ')
print ("hey", name)

print(type(name))


#######################################

name = input ("Hey, what is your name? ")
print ("Nice to meet you", name, ",good luck")
study = input("What did you major at? ")
print ("Nice!, do you have any Statistics or Math classes in", study,"?")
input()
score = float(input("and what was you GPA? "))

print ("So let's sum it up:\n You\'re", name," you studied", study,". with a GPA of ", score)
print ("So let's sum it up:\n You\'re %s you studied %s with a GPA of %r " % (
	name, study, score))