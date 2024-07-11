print ("** SECURE LOGIN  **")
userName = input("What is your username> ")
passWord = input("What is your password> ")
if userName == "chirag" and passWord == "arora":
  print("Welcome Chirag")
elif userName == "david" and passWord == "baldy":
  print("Welcome David")
else:
  print("wrong username or password!")