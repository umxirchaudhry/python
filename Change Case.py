while True:
    input_text = input("Enter Text to change case (or type 'done' to quit): ")
    if input_text.lower() == 'done':
      break

    if isinstance(input_text, str):
      print('Lower Case: ', input_text.lower())
      print('Upper Case: ', input_text.upper())
      print('Sentence Case: ', input_text.title())
      print('Toggle Case: ', input_text.swapcase())
      print('Capitalize Case: ', input_text.capitalize())
    else:
      print("Error: Please enter text only.")
