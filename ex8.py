# A (str) variable which contains 4 formatters
formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
		"I had this things",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight.")
)

print(type(formatter))