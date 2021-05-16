"""
main.py

  A simple console based chatbot that uses control flow and conditionals to provide
  pre-defined choices and responses.
"""

# Define your functions
def coffee_bot():
  # Welcome Message!
  print("\n=== Welcome to the Cafe! ===\n")
  size = get_size()
  drink_type = get_drink_type()
  # Order Summary:
  print(f"\nAlright, that's a {size} {drink_type}!")
  # Gather the User's Name:
  name = input("\nCan I get you name please? >>> ")
  # Conclusion Message:
  print(f"\nThanks, {name}! Your order will be ready shortly.\n\n")


# Ask for the drink size:
def get_size():
  res = input("""What size drink can I get for you?
  [s] Small
  [m] Medium
  [l] Large
\n>>> """
  )
  # Force to lowercase:
  res = res.lower()
  # Determine selection:
  if (res == 's'):
    return 'Small'
  elif (res == 'm'):
    return 'Medium'
  elif (res == 'l'):
    return 'Large'
  # Handle invalid input:
  else:
    print_error_message()
    return get_size()


# Ask for drink type:
def get_drink_type():
  res = input("""What type of drink would you like?
  [1] Brewed Coffee
  [2] Mocha
  [3] Latte
\n>>> """)
  # Force to integer:
  res = int(res)
  # Determine selection:
  if (res == 1):
    return 'Brewed Coffee'
  elif (res == 2):
    return 'Mocha'
  elif (res == 3):
    return order_latte()
  # Handle invalid input:
  else:
    print_error_message()
    return get_drink_type()


# Ask milk type for latte:
def order_latte():
  res = input("""And what kind of milk for your latte?
  [a] 2% milk
  [b] Non-fat milk
  [c] Soy milk
\n>>> """)
  # Force to lowercase:
  res = res.lower()
  # Determine selection:
  if (res == 'a'):
    return "Latte with 2% milk"
  elif (res == 'b'):
    return "Latte with Non-fat milk"
  elif (res == 'c'):
    return "Latte with Soy milk"
  # Handle invalid input:
  else:
    print_error_message()
    return order_latte()



# Sorry, invalid selection message:
def print_error_message():
  print("I'm sorry, I did not understand your selection.\nPlease enter the corresponding letter for your response.\n")


# Start our bot!
coffee_bot()
