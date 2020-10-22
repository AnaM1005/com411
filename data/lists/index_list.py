#Defining the functions movements
def movements():
  path = ["Move Forward", 
          10, 
          "Move Backward", 
          5, 
          "Move Left", 
          3, 
          "Move Right", 
          1]
  return path

def run():
  print("Moving...")
  path = movements()
  for index in range(0, len(path), 2):
     print("{} for {} steps.". format (path [index], path[index + 1]))
  
#Call to the function
run()