"""
main.py

  A simple console based chatbot that uses control flow and conditionals to provide
  pre-defined choices and responses.
"""

from utils import (
  print_error_message, 
  get_size, 
  order_mocha, 
  order_latte
)

from orders_list import get_current_order_number

print(get_current_order_number())

# Main Coffee Bot Function:
def coffee_bot():
  # Welcome Message!
  print("\n=== Welcome to the Cafe! ===\n")

  # List of drink names:
  drinks = []
  order_drink = 'y'
  # Loop to allow multiple drink orders:
  while (order_drink == 'y'):
    size = get_size()
    drink_type = get_drink_type()
    drink = f"{size} {drink_type}"
    # Add drink to list:
    drinks.append(drink)
    print(f"\nAlright, that'll be one {drink}!\n")
  
    # Order another drink?
    while True:
      order_drink = input("Would you like to order another drink? (y/n) >>> ")
      if (order_drink.lower() in ['y', 'n']):
        break

  # Review the drinks in the order:
  review = "\nOkay, so I have:\n"
  for d in drinks:
    review += " - ({}) {}\n".format(1, d)
    # TODO: Implement quantity to count the same drinks.
  print(review)

  # Gather the User's Name:
  name = input("\nCan I get you name please? >>> ")
  # Conclusion Message:
  print(f"\nThanks, {name}! Your order will be ready shortly.\n\n")


# Ask for drink type:
def get_drink_type():
  res = input("""What type of drink would you like?
  [1] Brewed Coffee
  [2] Mocha
  [3] Latte
\n>>> """)
  # Force to integer + Handle non-ints:
  try:
    res = int(res)
  except:
    print_error_message()
    return get_drink_type()

  # Determine selection:
  if (res == 1):
    return 'Brewed Coffee'
  elif (res == 2):
    return order_mocha()
  elif (res == 3):
    return order_latte()
  # Handle invalid input:
  else:
    print_error_message()
    return get_drink_type()


# Start up our bot!
coffee_bot()
