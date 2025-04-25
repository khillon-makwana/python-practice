#A program to find the sum of all the elements in a list
def mySum(numbers):
    total = 0

    for number in range(len(numbers)):
        total = total + numbers[number]
    return total

myList = [1,2,3,4]
print("The sum of the list is: ", mySum(myList))

list2 = [2,4,5,6]
print("The sum of the elements in the second list is: ", mySum(list2))