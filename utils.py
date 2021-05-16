"""
utils.py

  Utility functions our chatbot commonly uses to prompt the user at
  different parts of the ordering process.
"""

# Invalid Selection Message:
def print_error_message():
  print("***I'm sorry, I did not understand your selection.\nPlease enter the corresponding letter for your response.\n")


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
  

# Order Mocha --> Offer special edition:
def order_mocha():
  while True:
    res = input("""Would you like to try our limited-edition peppermint mocha?
    [y] Sure!
    [n] Maybe next time.
  \n>>> """
    )
    # Force to lowercase:
    res = res.lower()
    # Determine selection:
    if (res == 'y'):
      return 'Peppermint Mocha'
    elif (res == 'n'):
      return 'Mocha'
    # Handle invalid input:
    else:
      print_error_message()


# Order Latte --> Ask for milk type:
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
  