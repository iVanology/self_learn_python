####### Assignment for session on 9/18/2023
####### 3. Conditional structures (if)
#Solution to question 1
# Ask the fisher for the length of the zander
length = float(input("Please enter the length of the zander in centimeters: "))

# Check if it meet the requirement
if length < 42:
    difference = 42 - length
    print(f"The zander does not meet the size limit. \nPlease release it back into the lake. \nThe fish is {difference} centimeters below the size limit.")

else:
    print("The zander meets the size limit.")


########Solution to question 2
# Ask the user to enter the cabin class
cabin_class = input("Please enter the cabin class. Is it LUX, A, B, or C? \n")

# Check the cabin class using an if/elif/else structure
if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")



########Solution to question 3
# Ask the user for biological gender and hemoglobin value
gender = input("Please enter your biological gender (male or female): ").lower()
hemoglobin = float(input("Please enter your hemoglobin value (in g/l): "))

# Check the hemoglobin value based on gender using an if/elif/else structure
if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin value is low.")
    elif 117 <= hemoglobin <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin value is low.")
    elif 134 <= hemoglobin <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid biological gender entered.")


########Solution to question 4
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("A Leap Year.")
        else:
            print("Not a Leap Year.")
    else:
        print("A Leap Year")
else:
    print("Not a Leap Year.")


######## 4. While loops (while)
######## Solution to question 1
num = 1

# Use a while loop to iterate through numbers 1-1000
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1


######## Solution to question 2
while True:
    # Ask the user to input a value in inches
    inches = float(input("Please enter a value in inches: "))

    # Check if the input is negative
    if inches < 0:
        print("Your input is not valid. Program ended")
        break

    # Convert inches to centimeters
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters.")

######## Solution to question 3
import random

# Generate a random integer between 1 and 10
number_to_guess = random.randint(1, 10)

while True:
    # User tries to guess the number
    guess = int(input("Guess a number between 1 and 10: "))

    # Check the user's guess
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Correct!")
        break
