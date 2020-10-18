#The function
def identify():
  print("What lies ahead us?")
  response = input()

  #Display message
  if (response == "a large boulder"):
    print("It's time to run!")
  else:
    print("We will be fine.")

#Call to function
identify()
