# This script prompts the user to enter something and then determines if the input is an integer, a float, or a string.
# It continues to prompt for input until the user enters "done".

while True:  # Loop indefinitely
    user_input = input("Enter something: ")

    if user_input == 'done':
        break  # Exit the loop if the user enters "done"

    try:
        number = int(user_input) #Check if input is integer
        print('You entered an integer:', number)
    except ValueError:
        try:
          number = float(user_input) #Check if input is float
          print('You entered an float:', number)
        except ValueError:
          print('You entered a string:', user_input)

# Functions and Logics Used:
# - input(): Gets user input from the console.
# - int(): Converts a string to an integer.
# - float(): Converts a string to a float.
# - try-except block: Handles potential errors (ValueErrors in this case).
# - while loop: Repeats a block of code until a condition is met (in this case, until the user enters "done").
# - if and else statements: Control the flow of the program based on conditions. 