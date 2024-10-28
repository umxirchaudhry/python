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