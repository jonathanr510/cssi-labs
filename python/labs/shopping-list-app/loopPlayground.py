print("Welcome")

myString = raw_input("Give me a string loop through: ")

letterNum = 1


for character in myString:
    print("This is letter number %s" % (letterNum))
    letterNum = letterNum + 1
    print(character)
