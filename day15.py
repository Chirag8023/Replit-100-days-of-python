exit = "no"

print ("Do you like animal sounds, type in an animal below, I will tell you the sound")
print ("----------")
print ()

while exit == "no":
  animal = input ("What animal sound do you want to hear? ")

  if animal == "cow":
    print ("mooooooo")
  elif animal == "pig":
    print ("oink, oink, oink")
  elif animal == "sheep":
    print ("🐑 Baaa")
  elif animal == "duck":
    print("🦆 Quack")
  elif animal == "dog":
    print("🐶 Woof")
  elif animal == "cat":
    print("🐱 Meow")
  else: 
    print("I don't know that animal sound. Try again.")

  print ()
  exit = input ("Do you want to exit? ")