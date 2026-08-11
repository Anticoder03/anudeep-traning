# Write a program that uses an IF statement to print "Good morning" if the time is between 5 and 12 hours in a 24-hour format.
# Example: 2:00 PM will be 14 in 24-hour format.

# time = int(input("Enter the time in 24-hour format (0-23): "))
# if 5 <= time < 12:
#     print("Good morning")
    
    

# age = int(input("Enter your age: "))
# try:
#     age =  int(input("Enter your age: "))
#     if age >= 18:
#         print("You are eligible to vote.")
#     elif age < 18:
#         print("You are not eligible to vote yet.")
#     elif age < 0 or age > 120:
#         print("Invalid input. Please enter a valid age between 0 and 120.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer for age.")

# Create a "Magic Number Guessing" game. 
# Your code randomly generates a whole number between 0 to 20, example: 7 and does not disclose that number to you!
# You have to guess the number your code generated. 
# It asks you to find that number. If your guess matches your code's number then the While loop stops, and code says: "Congratulations!". Else, the code asks you to guess again. 
# Write code using a while loop.



# from random import randint


# magic_number = randint(0, 20)
# guess = None

# while guess != magic_number:
#     guess = int(input("Guess the magic number (0-20): "))
#     if guess < magic_number:
#         print("Too low! Try again.")
#     elif guess > magic_number:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the magic number.")

# Use a while loop to generate and print the first 100 odd numbers. 
# Also, print the sum of the first 100 odd numbers.
# count = 0
# odd_sum = 0
# odd_numbers = []

# while count < 100:
#     odd_number = 2 * count + 1
#     odd_numbers.append(odd_number)
#     odd_sum += odd_number
#     count += 1

# print("First 100 odd numbers:", odd_numbers)
# print("Sum of the first 100 odd numbers:", odd_sum)

numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
  print(numbers[index])
  index += 1
  
# fix it

