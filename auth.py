import sqlite3
import queries as q  
import hashlib 






def hash_password(raw_password):
  raw_password = raw_password.encode('utf-8')
  h = hashlib.sha256()
  h.update(raw_password)
  return h.hexdigest()


def signup():
  username = input("Pick a username: ")
  user = q.get_user_by_username(username)
  print(f"Signup: \n {user} \n {username}")
  while user is not None:
    username = input("You can surely be more creative than that =) Try again: ")
    user = q.get_user_by_username(username)
    
  password = input("Try to create password: ")
  while len(password) < 3:
    password = input("Try harder: ")

  hashed_password = hash_password(password)
  q.add_user(username, hashed_password)
  print(f"{username} user sucessfully created!")




def login():
  username = input("Enter your username: ")
  user = q.get_user_by_username(username)
  while user is None:
    username = input("Terrible name, try again: ")
    user = q.get_user_by_username(username)

  attempts = 5

  hashed_password = hash_password(input(f"Enter password for {username}: "))
  
  while hashed_password != user[4] and attempts > 0:
    print(attempts)
    if attempts > 3:
      msg = "Wrong password, try again!"
    elif attempts == 3:
      msg = "You really suck at this! Try again: "
    elif attempts == 2:
      msg = "I don't got all day pal: "
    elif attempts == 1:
      msg = "One last attempt, make it count =) : "
    else:
      msg = "Grevious error"
    hashed_password = hash_password(input(msg))
    attempts -= 1
  if attempts == 0:
    print("You suck! Get locked out of your account XD")
    return None
  print("Authenticated")
  return user


def authenticate():
  choice = input("1 - login\n2 - signup\nPick: ")

  while choice != "1" and choice != "2":
    choice = input("-_-\nPick:")
  if choice == "2":
    signup()

  return login()