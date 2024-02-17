import sqlite3
from auth import authenticate
import queries as q
from datetime import datetime

def settings():
  pass

def check_orders(user):
  id = user[0]
  orders = q.select_orders(id)

  print("Your orders:")
  for i, order in enumerate(orders):
    print(f"({i+1}) - {str(order[1]).ljust(10, ' ')} | ${str(order[2]).ljust(6, ' ')} | {str(order[3]).ljust(6, ' ')}")    
    
  order_number = int(input("Select an order: "))
  c_order = orders[order_number-1]
  print(f"{str(c_order[1]).ljust(10, ' ')} | ${str(c_order[2]).ljust(6, ' ')} | {str(c_order[3]).ljust(6, ' ')}" )
  
  choice = input("Remove order?")  
  if choice == "n":
    pass
  if choice == "y":
    q.update_cash(id, user[2] + c_order[2])
    q.remove_order(c_order[0])

def online_store(user):
  products = q.get_products()
  print("Here is the inventory: ")
  for i, product in enumerate(products):
    print(f"({i+1}) - {str(product[1]).ljust(10, ' ')} | ${str(product[2]).ljust(6, ' ')} | ${str(product[3]).ljust(6, ' ')}")
    
  product_number = int(input("Choose product: "))
  c_prod = products[product_number-1]
  
  product_price = c_prod[2]
  shipping_price = c_prod[3]
  total_price = product_price + shipping_price
  curr_cash = user[2]
  
  if total_price > curr_cash:
    print("You don't have enough")
  elif total_price <= curr_cash: 
    print("Making order. . .")
    timestamp = datetime.now()
    q.place_order(user[0], c_prod[0], timestamp)
    q.update_cash(user[0], curr_cash-total_price)
    print(f"Successfully purchased {str(c_prod[1])}!")
  else:
    print("Something has gone horribly wrong")


def work(user):
  id = user[0] 
  curr_cash = user[2]
  paycheck = 1200
  q.update_cash(id, curr_cash + paycheck)

def display_dashboard(id: int, username: str, cash: float):
  print("--------------------------------------------------------")
  print("DASHBOWARD")
  print(f"Hello, {username}. Proffer us your cash.")
  print(f"Balance: ${cash}")

def choose_action():

  msg = """
  What do you want to do? 
  (1) Proffer
  (2) Labor
  (3) Waste
  (4) Settings
  (5) Orders 
  (6) Oblivion
  """
  return input(msg)
  
  
  

def game():

  user = authenticate()
  if user is None:
    exit(0)

  while True:
    
    user = q.get_user_by_id(user[0])
    if user is None: exit(1)
    display_dashboard(user[0], user[1], user[2])
    choice = choose_action()
    
    match choice:
      case "1":
        online_store(user)
      case "2":
        work(user)
      case "3":
        print("Congratulations! Your death is closer than before!!")
      case "4":
        settings()
      case "5":
        check_orders(user)
      case "6":
        break
      case _:
        print("-_-")
    



if __name__ == "__main__":
  game()

