def directions():
  directions =["Move Forward", 
               "Move Backward", 
               "Turn Left", 
               "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  direct = directions()

  for index in range(len(direct)):
    print("{}: {}". format(index, direct[index]))
  
  direction_index = int(input())
  return direct[direction_index]

def run():
  route = []
  print("Working out escape route...")
  
  for count in range(5):
    direction = menu()
    route.append(direction)
  
  print("Escape route: {}.". format(route))

run()