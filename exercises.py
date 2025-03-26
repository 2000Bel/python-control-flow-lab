# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    letter = input("Enter a letter: ").strip()
    
    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single letter (a-z or A-Z).")
        return

    normalized = letter.lower()
    vowels = "aeiou"
    
    if normalized in vowels:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Invalid age. Age cannot be negative.")
            return
        
        voting_age = 18
        
        if age >= voting_age:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote yet.")
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")

check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    try:
        age = int(input("Input a dog's age: "))
        
        if age < 0:
            print("Invalid age. Age cannot be negative.")
            return
        
        if age == 0:
            print("The dog's age in dog years is 0.")
            return

        if age == 1:
            dog_years = 10
        elif age == 2:
            dog_years = 20
        else:
            dog_years = 20 + (age - 2) * 7
        
        print(f"The dog's age in dog years is {dog_years}.")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    cold = input("Is it cold? (yes/no): ").strip().lower()
    raining = input("Is it raining? (yes/no): ").strip().lower()
    
    if cold not in ("yes", "no") or raining not in ("yes", "no"):
        print("Invalid input. Please enter 'yes' or 'no'.")
        return
    
    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():

    seasons = {
        "Winter": [("Dec", 21, 31), ("Jan", 1, 31), ("Feb", 1, 28), ("Mar", 1, 19)],
        "Spring": [("Mar", 20, 31), ("Apr", 1, 30), ("May", 1, 31), ("Jun", 1, 20)],
        "Summer": [("Jun", 21, 30), ("Jul", 1, 31), ("Aug", 1, 31), ("Sep", 1, 21)],
        "Fall": [("Sep", 22, 30), ("Oct", 1, 31), ("Nov", 1, 30), ("Dec", 1, 20)],
    }
    
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    try:
        day = int(input("Enter the day of the month: ").strip())
    except ValueError:
        print("Invalid day. Please enter a number.")
        return

    valid_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    days_in_month = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30,
                     "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31}

    if month not in valid_months:
        print("Invalid month. Please enter a three-letter month abbreviation (e.g., Jan, Feb).")
        return

    if day < 1 or day > days_in_month[month]:
        print(f"Invalid day. {month} has {days_in_month[month]} days.")
        return

    for season, date_ranges in seasons.items():
        for m, start_day, end_day in date_ranges:
            if month == m and start_day <= day <= end_day:
                print(f"{month} {day} is in {season}.")
                return

determine_season()

# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    target_number = 42  # Fixed number to guess
    max_attempts = 5  # Maximum number of guesses

    print("Guess the number (between 1 and 100). You have 5 attempts.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: ").strip())

            if guess < 1 or guess > 100:
                print("Invalid guess. Please enter a number between 1 and 100.")
                continue  
            
            if guess == target_number:
                print("Congratulations, you guessed correctly!")
                return

            if guess < target_number:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")

            if attempt == max_attempts:
                print("Sorry, you failed to guess the number in five attempts.")
            elif attempt == max_attempts - 1:
                print("Last chance!")

        except ValueError:
            print("Invalid input. Please enter a number.")

guess_number()

