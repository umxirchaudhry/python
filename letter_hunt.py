# This script allows the user to repeatedly search for a word within the string "banana". 
# The user can enter any word, and the script will tell them if the word is found and its position. 
# The script continues to prompt for input until the user enters "done", at which point it exits.

while True:  # Start an infinite loop
  user_input = input('Help me to find in Banana: ')  # Get user input

  # Check if the user wants to quit
  if user_input.lower() == 'done': 
    print('Good Buy')  # Print a goodbye message
    break  # Exit the loop


  # Convert the user input to lowercase for case-insensitive search
  fruit = 'banana'  # Define the word to search in
  pos = fruit.find(user_input.lower())  # Find the position of the input in the word


  # Check if the input was found
  if pos >= 0:
    print('We have found it @ pos:', pos)  # Print the position if found
    print('\n') # Add line gap
  else:
    print('Not Found')  # Print "Not Found" if not found
    print('\n') # Add line gap


# Functions used:
# - input(): Prompts the user for input and returns the entered text.
# - lower(): Converts a string to lowercase.
# - find(): Searches for a substring within a string and returns its starting index if found, or -1 if not found.
# - print(): Displays output to the console.
# - break: Exits the loop.

# Logic used:
# - Looping: The `while True` statement creates an infinite loop.
# - Conditional statements: The `if` and `else` statements check for specific conditions and execute different code blocks based on the results.
# - String manipulation: The `lower()` and `find()` methods are used to manipulate strings and search for substrings.