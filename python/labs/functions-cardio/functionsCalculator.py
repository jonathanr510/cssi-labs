print("Welcome to your favorite calculator")

num1 = int(raw_input("Give me a numero: "))
num2 = int(raw_input("Give me another numero: "))

def myAddFunction(add1, add2):
    sum = add1 + add2
    return sum

print("Here is the sum: " + str(myAddFunction(num1, num2)))
