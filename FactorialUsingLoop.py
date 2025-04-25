# A program to calculate the factorial of a number using loops
def factorialLoop(number):
    answer = 1
    while number > 0:
        answer = answer * number
        number = number - 1
    return answer

userinput = int(input("Enter a number: "))
print(f"{userinput}! is",factorialLoop(userinput))