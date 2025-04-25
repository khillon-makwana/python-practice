# A python program to determine whether a number is odd or even

def numberChecker():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"The number {number} is an even number.")
    else:
        print(f"The number {number} is an odd number.")

numberChecker()