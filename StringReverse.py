# A program to reverse a string
def stringReverse(element):
    reversedString = ""

    for i in element:
        reversedString = i + reversedString
    return reversedString


userinput = input("Enter a string to reverse: ")
print(f"{userinput} when reversed gives:", stringReverse(userinput))