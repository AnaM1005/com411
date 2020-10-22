#Define the function
def directions():
  directions = ["Move Forward",
                "Move Backward", 
                "Turn Left", 
                "Turn Right"]
  return directions

def menu():
  print("Please select the direction:")
  direct = directions()
  for index in range(len(direct)):
    print("{} : {}".format(index, direct[index]))

def run():
  menu()

run()


