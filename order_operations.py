"""
orders_operations.py

  Where we handle our order queue and database operations.
"""
# TODO: Set Up MongoDB Connection via URI

from replit import db

'''
def init_db_values():
  # Initial Order Number
  db['_ORDER_NUMBER'] = 100000
'''    

def submit_new_order(order_number: int, order: object):
  # {'order_######': {} }                 # TODO: Determine a structure for the order object.
  db[f"order_{order_number}"] = order


# Returns the current order number:
def get_current_order_number():
  return db['_ORDER_NUMBER']


# Set the current order number:
def set_current_order_number(num: int):
  db['_ORDER_NUMBER'] = num
  return None


# Generates & Sets the next consecutive order number:
def generate_next_order_number():
  current_num = get_current_order_number()
  set_current_order_number(current_num + 1)
  return get_current_order_number()
