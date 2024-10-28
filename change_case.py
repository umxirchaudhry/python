# This script prompts the user to enter text and then displays various case conversions of the input.
# It continues to prompt for input until the user types "done".

while True:
    # Get user input
    input_text = input("Enter Text to change case (or type 'done' to quit): ")
    
    # Check if the user wants to quit
    if input_text.lower() == 'done':
      break

    # Check if the input is a string
    if isinstance(input_text, str):
      # Print the different case conversions
      print('Lower Case: ', input_text.lower())
      print('Upper Case: ', input_text.upper())
      print('Sentence Case: ', input_text.title())
      print('Toggle Case: ', input_text.swapcase())
      print('Capitalize Case: ', input_text.capitalize())
    else:
      # Print an error message if the input is not a string
      print("Error: Please enter text only.")

# Functions and Logics Used:
# - input(): Gets user input from the console.
# - lower(): Converts a string to lowercase.
# - upper(): Converts a string to uppercase.
# - title(): Converts a string to sentence case (first letter of each word capitalized).
# - swapcase(): Swaps the case of characters in a string (lowercase to uppercase and vice versa).
# - capitalize(): Capitalizes the first letter of a string.
# - isinstance(): Checks the type of an object.
# - while loop: Repeats a block of code until a condition is met (in this case, until the user enters "done").
# - if and else statements: Control the flow of the program based on conditions. 
