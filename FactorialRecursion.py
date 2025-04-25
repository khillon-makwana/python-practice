#A program to find the factorial of a number using recursion

def factorialRecursion(number):
    if number == 0:
        return 1
    else:
        return number * factorialRecursion(number - 1)

userinput = int(input("Enter a number: "))
print(f"{userinput}! is:", factorialRecursion(userinput))