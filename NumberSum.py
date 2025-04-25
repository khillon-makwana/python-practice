#A program to calculate the sum of digits in a number
def numSum(number):
    total = 0
    for i in number:
        total = total + int(i)
    return total

userinput = input("Enter a number: ")
print(f"The sum of the individual numbers in {userinput} is:",numSum(userinput))

