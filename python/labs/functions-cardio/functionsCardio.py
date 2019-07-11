# print("Welcom to Functions Cardio")
#
# num1 = int(raw_input("Enter side 1 length: "))
# num2 = int(raw_input("Enter side 2 length: "))
# num3 = int(raw_input("Enter side 3 length: "))
#
#
# def is_triangle(s1, s2, s3):
#     sum1 = s1 + s2
#     sum2 = s2 + s3
#     sum3 = s3 + s1
#     if sum1 > s3 and sum2 > s1 and sum3 > s2:
#         print("You have a triangle")
#         return True
#     else:
#         print("You have no triangle")
#         return False
#
# is_triangle(num1, num2, num3)

num1 = raw_input("give me a word: ")

def reverse_string(word1):
    word1 = word1[::-]
    print(word1)
    return word1

    reverse_string(num1)
