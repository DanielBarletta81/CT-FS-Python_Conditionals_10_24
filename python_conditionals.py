#Task 1: Code Correction You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

#Buggy Code:

""" number = input("Enter a number: ")
if number > 0:
    print("The number is positive.")
elif number = 0:
    print("The number is zero.")
else number < 0:
    print("The number is negative.") """

#Corrected Code ~~~~~~

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#2
#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers.
# Your code should then identify and print out the largest number among the three.

#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine
#  the smallest number among the three and print it out.

#Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that 
# "The smallest number is 3. The largest number is 4. "


number1 = input('Enter your first number: ')
number2 = input('Enter your next number: ')
number3 = input('Enter your last number: ')

if (number1 >= number2) and (number1 >= number3):
    print(f'The largest number is: {number1}.')

elif (number2 >= number1) and (number2 >= number3):
    print(f'The largest number is: {number2}.')
else:
    print(f'The largest number is: {number3}.')



#Task 2.2: Identify the Smallest

if (number1 <=  number2) and (number1 <= number3):
     print(f'The smallest number is: {number1}.')

elif (number2 <= number1) and ( number2 <= number3):
     print(f'The smallest number is: {number2}.')
else:
     print(f'The largest number is: {number3}.')








